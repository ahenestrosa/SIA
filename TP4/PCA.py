from Utils import utils
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


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

print()

components = pca_factory.fit(valuesStd)
print(components.components_[0]) #this shows the influence of every variable in the first component
#[ 0.1248739  -0.50050586  0.40651815 -0.48287333  0.18811162 -0.47570355 0.27165582]

first_component = Y[:,0]
second_component = Y[:,1]
scalex = 1.0 / (first_component.max() - first_component.min())
scaley = 1.0 / (second_component.max() - second_component.min())

coeff = np.transpose(components.components_[0:2, :])
n = coeff.shape[0]

variables = ["Area", "GDP", "Inflation", "Life Expectancy", "Military", "Pop Growth", "Unemployment"]

#https://stackoverflow.com/questions/39216897/plot-pca-loadings-and-loading-in-biplot-in-sklearn-like-rs-autoplot

plt.scatter(first_component * scalex, second_component * scaley)

print(variables)
for i in range(n):
        plt.arrow(0, 0, coeff[i,0], coeff[i,1],color = 'r',alpha = 0.5)
        plt.text(coeff[i,0]* 1.15, coeff[i,1] * 1.15, variables[i], color = 'g', ha = 'center', va = 'center')

plt.xlim(-1,1)
plt.ylim(-1,1)
plt.xlabel("First Component")
plt.ylabel("Second Component")
plt.grid()




# for i, txt in enumerate(countries):
#     ax.annotate(txt, (first_component[i], second_component[i]))
# we did not show names as points are very close

plt.show()




