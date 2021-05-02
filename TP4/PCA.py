from Utils import utils
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np


filePath = "/Users/franciscochoi/Desktop/SIA/TP4/Resources/europe.csv"

matrix = pd.read_csv(filePath)

values = matrix.iloc[:,1:8].values #only values
countries = matrix.iloc[:, 0].values #only country names

valuesStd = StandardScaler().fit_transform(values) #standarization of values --> z = (x - u) / s
valuesCov = np.cov(valuesStd.T) #we need transposed matrix as numpy calculates the array as X = [x_1, x_2, ... x_N]^T

autoVal, autoVec = np.linalg.eigh(valuesCov)

pca = PCA().fit(valuesStd)

# print(valuesCov)

# print(np.cumsum(pca.explained_variance_ratio_))  #
#[0.46102367 0.63061273 0.78249709 0.89254794 0.95795489 0.982051161]

pca_factory = PCA(n_components=5) #0.96 covered
Y = pca_factory.fit_transform(valuesStd)

print(Y[:,0:2])




