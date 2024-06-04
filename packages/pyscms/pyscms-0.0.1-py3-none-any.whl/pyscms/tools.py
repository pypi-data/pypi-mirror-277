import numpy as np
import pandas as pd
from scipy import sparse
import matplotlib.pyplot as plt
from functools import reduce
import os
import pickle
import sys
from sklearn.feature_selection import SelectKBest, chi2, f_classif
from sklearn.model_selection import train_test_split, cross_validate ,cross_val_score, GridSearchCV
from sklearn.svm import SVC
from sklearn.linear_model import LassoCV, Lasso, LogisticRegression
from bayes_opt import BayesianOptimization
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, Normalizer
from sklearn.metrics import classification_report
from tqdm import tqdm

#https://packaging.python.org/en/latest/tutorials/packaging-projects/
## 训练随机森林模型并保存
def rf_model(X_train, Y_train, modelPath):
    from sklearn.ensemble import RandomForestClassifier
    clf = Pipeline([('scale', Normalizer()),
                    ('rf', RandomForestClassifier(n_jobs=-1,
                                                  n_estimators=600,
                                                  max_features=50,
                                                  random_state=100))])
    clf.fit(X_train, Y_train)
    f = open(modelPath, 'wb')
    pickle.dump(clf, f)
    f.close()
    return clf

## 获取前多少的特征名称
def get_feature(modelPath, modelname='rf', topn=50):
    f = open(modelPath, 'rb')
    clf = pickle.load(f)
    f.close()
    imp = clf[modelname].feature_importances_
    ## 获取前50个特征
    index = np.argsort(imp)[::-1][:topn]
    return index

## 挑选特征
def selectFeature(Xdata, Ydata, clf, k):
    '''
    :param Xdata: 特征数据
    :param Ydata: 标签数据
    :param clf: 模型
    :param k: 多少个特征
    :return:
    '''
    X_train, X_test, \
        Y_train, Y_test = train_test_split(Xdata, Ydata,
                                           random_state=100, test_size=0.2)
    ###支持向量机
    # clf = SVC()
    select = SelectKBest(chi2, k=k)
    z = select.fit_transform(X_train, Y_train)
    featureIndex = select.get_support()
    features = X_train.columns[featureIndex]
    X_train = X_train.iloc[:, featureIndex]
    X_test = X_test.iloc[:, featureIndex]
    clf.fit(X_train, Y_train)
    trainScore = round(clf.score(X_train, Y_train), 4)
    testScore = round(clf.score(X_test, Y_test), 4)
    return {k:(trainScore,
               testScore,
               features)}

### 用以将各种数据格式进行转换, 统一将df转为稀疏矩阵在处理, 行统一对应mz， 列统一为barcode
class dataset():
    def __init__(self, dataPath, savePath,
                 groupName='nogroup',
                 dataType='sparse',
                 mzlist=None,
                 barcode=None,
                 cellpos=None,
                 cellprob=None):
        '''
        :param dataPath: 读入文件路径
        :param savePath:
        :param dataType:
        :param saveType:
        :param groupName: 数据对应的分组名称
        :param mzlist: mz列表
        :param barcode: 每个细胞对应的名称
        '''
        if os.path.isfile(dataPath):
            self.dataPath = dataPath
        else:
            print(dataPath, 'is not exist!')
        ## 加入文件名前缀
        self.filename = os.path.basename(dataPath).split('.')[0]
        print(self.filename)
        self.savePath = savePath
        self.groupName = groupName
        if dataType == 'sparse':
            self.load_sparse(mzlist=mzlist,
                             barcode=barcode,
                             cellpos=cellpos,
                             cellprob=cellprob)
        elif dataType == 'csv':
            self.load_dataframe()
        else:
            pass

    def load_sparse(self, mzlist, barcode, cellpos, cellprob, T=True):
        self.df = sparse.load_npz(self.dataPath)
        self.df = self.df.astype('int')
        ##默认做转制
        if T:
            self.df = self.df.T
        if mzlist is None:
            ## 跟mzdb.savevalue的保持一致
            mzlist = list(range(100, 1000 + 1))
        self.mz = mzlist
        if barcode is None:
            barcode = [str(i) for i in range(1, self.df.shape[1]+1)]
        if not cellpos is None:
            barcode = [i+'-cell' if i in cellpos else i+'-null' for i in barcode]
        ## 在barcode加入概率
        if not cellprob is None:
            barcode = [barcode[i] + '-' + str(cellprob[i]) for i in range(len(barcode))]
        ## 在barcode最后加入文件名
        barcode = ['-'.join([str(i), self.groupName, self.filename]) for i in barcode]
        self.barcode = barcode

    def load_dataframe(self, fillna=False):
        self.df = pd.read_csv(self.dataPath)
        if fillna:
            self.df.fillna(0, inplace=True)
        self.mz = self.df.index.to_list()
        self.barcode = self.df.columns.to_list()
        self.df = coo_matrix(self.df.values.astype(int))

    def save_seurat(self, mzRound=2):
        '''
        :param meta: index为mz，columns包含细胞位置、分组信息
        :param outputDir:
        :return:
        '''
        self.feature = ['mz' + str(round(float(i), mzRound)) for i in self.mz]
        ## 保存
        io.mmwrite(os.path.join(self.savePath, 'matrix.mtx'), self.df)
        with open(os.path.join(self.savePath, 'matrix.mtx'), 'rb') as mtx_in:
            with gzip.open(os.path.join(self.savePath, 'matrix.mtx.gz'), 'wb') as mtx_gz:
                shutil.copyfileobj(mtx_in, mtx_gz)
        barcode = pd.DataFrame(self.barcode)
        barcode.to_csv(os.path.join(self.savePath, 'barcodes.tsv.gz'), sep='\t', header=False, index=False)
        feature = pd.DataFrame(self.feature)
        feature.to_csv(os.path.join(self.savePath, 'features.tsv.gz'), sep='\t', header=False, index=False)

    ## 根据mzml路径、细胞位置和文件对应的组名提取数据，默认要求至少在3个细胞里测到物质
    def cellSignal(self, mzMLPath, pos, groupName,
                   filerMZ = 3):
        mzml_file = pyteomics.mzml.MzML(mzMLPath)
        i = 1
        pos = [int(j) for j in pos]
        xList = []
        for spectrum in mzml_file:
            if i in pos:
                df = mzMlDf(spectrum, number=i)
                xList.append(df)
            i += 1
        xDf = merge(xList)
        all = xDf.notna().sum(axis=1)
        index = all >= filerMZ
        xDf = xDf[index]
        xDf.columns = groupName + '-' + xDf.columns
        return xDf

class model():
    def __init__(self, modelPath=None):
        self.modelDict = {
            'svm': self.svm,
            'lasso': self.lasso
        }
        if not modelPath is None:
            if os.path.isfile(modelPath):
                f = open(modelPath, 'rb')
                self.clf = pickle.load(f)
                f.close()
            else:
                print(modelPath, 'is not avalible!')
    def svm(self, c=1, gamma='scale'):
        return Pipeline([
            ('scale', Normalizer()),
            ('svm', SVC(
                probability=True,
                kernel='rbf',
                C=c,
                gamma=gamma
            )
             )
        ])
    def lasso(self, c=1):
        return Pipeline([
            ('scaler', Normalizer()),
            ('lasso', LogisticRegression(
                penalty='l1', solver="saga", C=c))
        ])

class ml():
    def __init__(self, xdata, ydata=None,
                 modelPath=None,
                 modelparam=None):
        self.model = model(modelPath=modelPath)
        self.clf = self.model.clf
        self.xdata = xdata
        self.ydata = ydata
        if not ydata is None:
            index = np.arange(1, len(ydata) + 1)
            [self.X_train, self.X_test,
            self.Y_train, self.Y_test,
            self.id_train, self.id_test] = train_test_split(xdata, ydata, index,
                                                 random_state=100, test_size=0.2)
        self.params = modelparam

    def train(self, model='lasso'):
        self.clf = self.model.modelDict[model]()
        if not self.params is None:
            self.clf.set_params(**self.params)
        self.clf.fit(self.X_train, self.Y_train)

    def test(self):
        yPre = self.clf.predict(self.X_test)
        self.report = classification_report(self.Y_test, yPre)

    def tune(self,
             params_range={'c': (1e-3, 0.9)}):
        def lasso_cv(c):
            val = cross_val_score(
                self.model.modelDict['lasso'](c=c),
                self.X_train, self.Y_train,
                scoring='f1', cv=5
                ).mean()
            return val
        lasso_bo = BayesianOptimization(
            lasso_cv,
            params_range
        )
        lasso_bo.maximize()
        self.params = {
            'lasso__C':lasso_bo.max['params']['c']
        }

    def saveModel(self, modelPath):
        f = open(modelPath, 'wb')
        pickle.dump(self.clf, f)
        f.close()

    def getFeature(self,
                   featureList=np.arange(100, 1001)):
        index = self.clf['lasso'].coef_ != 0
        featureDict = {'feature':featureList[index[0]],
                        'coef':self.clf['lasso'].coef_[index]}
        return featureDict

    ### 用于利用模型预测数据集
    def predictCell(self, fileName=None, predict_file=None, label=False):
        '''
        :param fileName: 预测的数据集名称
        :param predict_file: 保存结果的名称
        :return:
        '''
        result = self.clf.predict(self.xdata)
        pos = np.arange(1, len(result) + 1)[result == 1]
        self.pos = pos
        num = len(pos)
        if num == 0:
            pos = '0'
        else:
            pos = [str(j) for j in pos]
            pos = ','.join(pos)
        ## 如果需要输出标签
        if label:
            self.pos = result
            pos = ','.join([str(j) for j in result])
        if fileName is None or predict_file is None:
            return self.pos
        else:
            print(fileName)
            with open(predict_file, 'a') as f:
                f.write(fileName + '\n')
                f.write(str(num) + '\n')
                f.write(pos + '\n')
                f.flush()
    ### 输出预测概率值
    def predictProb(self, fileName=None, predict_file=None):
        prob = self.clf.predict_proba(self.xdata)
        probMax = prob.max(axis=1).round(3)
        if fileName is None or predict_file is None:
            return probMax
        else:
            print(fileName)
            probMax = ','.join([str(j) for j in probMax])
            with open(predict_file, 'a') as f:
                f.write(fileName + '\n')
                f.write(probMax + '\n')
                f.flush()

class mzml():
    def __init__(self, mzfile, mzround=2):
        if not os.path.isfile(mzfile):
            print(mzfile, 'is not exit')
        self.mzround = mzround
        self.mzfile = mzfile
        self.spectrum = []
        self.dataDict={
            'mz' : [],
            'ins' : []
        }

## 根据离子列表提取质谱数据
    def list(self, mzlist):
        '''
        选择list内的质谱图
        :param mzlist:
        :return:
        '''
        mzml_file = pyteomics.mzml.MzML(self.mzfile)
        i = 0
        for spectrum in mzml_file:
            i += 1
            if i in mzlist:
                self.spectrum.append(spectrum)
        ##返回最大帧数
        self.max = i

## 根据最大值最小值提取质谱数据
    ## 默认就是获取全部， 其中stop无限大
    def range(self, start=1, stop=1e9):
        mzml_file = pyteomics.mzml.MzML(self.mzfile)
        i = 0
        for spectrum in mzml_file:
            i += 1
            if i>=start and i<=stop:
                self.spectrum.append(spectrum)
        ##返回最大帧数
        self.max = i

    def spectrumData(self):
        for spectrum in tqdm(self.spectrum):
            self.dataDict['mz'].append(spectrum["m/z array"])
            self.dataDict['ins'].append(spectrum["intensity array"])

    def mergeDf(self, bindata=False):
        xList = []
        for i in tqdm(range(len(self.dataDict['mz']))):
            mz = self.dataDict['mz'][i]
            intensity = self.dataDict['ins'][i]
            ## 默认不做bin处理
            if bindata:
                bins = bin(data=mz, start=100)
                df = pd.DataFrame(data={'bins': bins,
                                        'ins': intensity})
                ## 这里默认对bin进行求和处理
                df = df.groupby('bins').sum()
            else:
                peaks, _ = find_peaks(intensity)
                df = pd.DataFrame(data={'mz': mz[peaks].round(self.mzround),
                                        'ins': intensity[peaks].round(1)})
                df = df.groupby('mz').max()
            df.columns = [str(i)]
            xList.append(df)
        self.mzDf = merge(xList)

class mzdb():
    def __init__(self, mzfile, mzlist=None,
                 backgroundMz=None, mzround=2,
                 bindata=False):
        self.targetmz = mzml(mzfile=mzfile, mzround=mzround)
        self.background = mzml(mzfile=mzfile, mzround=mzround)
        self.tarback = mzml(mzfile=mzfile, mzround=mzround)
        self.mzlist = mzlist
        self.backgroundMz = backgroundMz
        self.bindata = bindata
## 仅提取目标帧
    def getTarget(self):
        self.targetmz.list(mzlist=self.mzlist)
        self.targetmz.spectrumData()
        self.targetmz.mergeDf(bindata=self.bindata)
## 提取背景帧
    def getBackground(self):
        ## 如果没有目标帧，那么背景帧就是全部帧
        if self.mzlist is None:
            mzlist = [0,]
        else:
            mzlist = self.mzlist
        ## 如果没有给出背景帧位置，则提取除目标帧以外的背景帧
        if self.backgroundMz is None:
            self.backgroundMz = [i for i in tqdm(range(1, self.targetmz.max)) if i not in mzlist]
        self.background.list(mzlist=self.backgroundMz)
        self.background.spectrumData()
        self.background.mergeDf(bindata=self.bindata)

### 分别处理目标帧和背景帧
    def getValue(self):
        self.getTarget()
        self.getBackground()

### 同时提取范围内的目标帧和背景帧, 如果mzlist为空则不区分目标和背景，同背景帧
    def getTarBack(self, start=1,  stop=None):
        if stop is None:
            self.tarback.range(start=start)
            stop = self.tarback.max
        else:
            self.tarback.range(start=start, stop=stop)
        self.tarback.spectrumData()
        self.tarback.mergeDf(bindata=self.bindata)
        self.tarback.mzDf.fillna(value=0, inplace=True)
        if not self.mzlist is None:
            ###把mzlist转成带01的列表
            self.label = np.zeros(stop-start+1)
            pos = self.mzlist[(self.mzlist<=stop) & (self.mzlist>=start)]
            self.label[pos-start] = 1

    def savevalue(self, savePath, mzmlName):
        ## 保存整数
        self.tarback.mzDf = round(self.tarback.mzDf)
        ## 调整荷质比范围
        if self.bindata :
            self.tarback.mzDf = self.tarback.mzDf.reindex(
                list(range(100, 1000 + 1)),
                fill_value=0)
        dfions = sparse.csr_matrix(self.tarback.mzDf.values.T)
        sparse.save_npz(os.path.join(savePath, mzmlName+".npz"), dfions)
        if not self.mzlist is None:
            np.save(os.path.join(savePath, mzmlName + '.npy'), self.label)


## 自动分割bin
def bin(data, bin_width=1, start=1):
    '''
    :param data:
    :param bin_width:
    :param start: 默认从1开始
    :return:
    '''
    bins = np.arange(data.min(), data.max(), bin_width)
    # 对数据划分成bin
    bin_number = np.digitize(data, bins) + start -1
    # 输出每个值所在的bin
    return bin_number

## 绘制原始质谱图
def plotmzml(spectrum, figureName):
    plt.figure(figsize=(30, 6))
    plt.plot(spectrum["m/z array"], spectrum["intensity array"])
    plt.savefig(figureName)
    plt.close()

## 绘制划bin后的质谱图
def plotmzml_df(df, figureName):
    plt.figure(figsize=(30, 6))
    plt.plot(df.index, df['ins'])
    plt.savefig(figureName)
    plt.close()

## 合并多个dataframe

# def merge(dataList, how='outer'):
#     df_merge = reduce(lambda left, right: pd.merge(left, right, left_index=True, right_index=True,
#                                         how=how), dataList)
#     return df_merge


## 加进度条
def merge_bar(pbar, left, right,
              how='outer'):
    # 更新进度条
    pbar.update(1)
    # 累积运算
    return pd.merge(left, right,
                    left_index=True,
                    right_index=True,
                    how=how)
def mergeList(dataList):
    # 创建进度条
    pbar = tqdm(total=len(dataList))
    # 使用reduce和自定义累积函数进行累积运算
    result = reduce(lambda left, right: merge_bar(pbar,
                                                  left,
                                                  right),
                    dataList)
    # 关闭进度条
    pbar.close()
    return result

def merge(dataList, chunk_size=500):
    newlist = []
    for dfs in chunk_dfs(dataList,
                         chunk_size=chunk_size):
        newlist.append(mergeList(dfs))
    return mergeList(newlist)

# def merge(dataList, on,how='outer'):
#     df_merge = reduce(lambda left, right: pd.merge(left, right, on=on,
#                                                    how=how), dataList)
#     return df_merge

### 将数据框分批
def chunk_dfs(dataList, chunk_size):
    """" yields n dataframes at a time where n == chunksize """
    dfs = []
    for f in dataList:
        dfs.append(f)
        if len(dfs) == chunk_size:
            yield dfs
            dfs  = []
    if dfs:
        yield dfs


import shutil
import pyteomics.mzml
from scipy.signal import find_peaks
from scipy.sparse import coo_matrix
from scipy import io
import gzip

## 将dataframe转成seurat的读入数据
def df2seurat(meta, outputDir):
    '''
    :param meta: index为mz，columns包含细胞位置、分组信息
    :param outputDir:
    :return:
    '''
    meta.index = 'mz' + np.round(meta.index, 2).astype('str')
    meta.fillna(0, inplace=True)
    mtx = coo_matrix(meta.values.astype(int))
    io.mmwrite(os.path.join(outputDir, 'matrix.mtx'), mtx)
    with open(os.path.join(outputDir, 'matrix.mtx'), 'rb') as mtx_in:
        with gzip.open(os.path.join(outputDir, 'matrix.mtx.gz'), 'wb') as mtx_gz:
            shutil.copyfileobj(mtx_in, mtx_gz)
    barcode = pd.DataFrame(meta.columns)
    barcode.to_csv(os.path.join(outputDir, 'barcodes.tsv.gz'), sep='\t', header=False, index=False)
    feature = pd.DataFrame(meta.index)
    feature.to_csv(os.path.join(outputDir, 'features.tsv.gz'), sep='\t', header=False, index=False)

## 根据mzml路径、细胞位置和文件对应的组名提取数据，默认要求至少在3个细胞里测到物质
def cellSignal(mzMLPath, pos, groupName,
               filerMZ = 3):
    mzml_file = pyteomics.mzml.MzML(mzMLPath)
    i = 1
    pos = [int(j) for j in pos]
    xList = []
    for spectrum in mzml_file:
        if i in pos:
            df = mzMlDf(spectrum, number=i)
            xList.append(df)
        i += 1
    xDf = merge(xList)
    all = xDf.notna().sum(axis=1)
    index = all >= filerMZ
    xDf = xDf[index]
    xDf.columns = groupName + '-' + xDf.columns
    return xDf

## 获取单个帧的质谱数据
def mzMlDf(spectrum, number):
    mz = spectrum['m/z array']
    intensity = spectrum['intensity array']
    peaks, _ = find_peaks(intensity)
    df = pd.DataFrame(data={'mz': mz[peaks].round(2),
                            'ins': intensity[peaks].round(1)})
    df = df.groupby('mz').max()
    df.columns = [str(number)]
    return df

class mz2seurat():
    def __init__(self, mzmlList, posList, groupNameList, outputDir):
        self.outputDir = outputDir
        dfList = []
        for mzml, pos, group in zip(mzmlList, posList, groupNameList):
            dfList.append(self.cellSignal(mzMLPath=mzml, pos=pos, groupName=group))
        self.meta = merge(dfList)
        self.df2seurat()

# 将字节数转换为 MB 的函数
def convert_bytes_to_mb(bytes):
    return round(bytes / (1024 * 1024), 2)
def statsData(current_directory):
    import os
    import pandas as pd
    # 初始化空列表，用于存储文件信息
    file_info = []
    # 遍历当前文件夹及其子目录下的所有文件
    for root, dirs, files in os.walk(current_directory):
        for file in files:
            # 获取文件相对路径
            file_path = os.path.join(root, file)
            # 获取子目录名
            subdirectory = os.path.basename(root)
            # 获取文件名
            filename = file
            # 获取文件大小（以字节为单位）
            file_size = os.path.getsize(file_path)
            file_size = convert_bytes_to_mb(file_size)
            # 将文件信息添加到列表中
            file_info.append({'Subdirectory': subdirectory,
                              'Filename': filename,
                              'File Size(MB)': file_size})
    # 将文件信息列表转换为 DataFrame
    return pd.DataFrame(file_info)