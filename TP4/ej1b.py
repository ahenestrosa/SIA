from Oja import Oja
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA



filePath = "/Users/franciscochoi/Desktop/SIA/TP4/Resources/europe.csv"

matrix = pd.read_csv(filePath)

values = matrix.iloc[:,1:8].values #only values
countries = matrix.iloc[:, 0].values #only country names
varHeaders = [c for c in matrix.columns if c != 'Country']

valuesStdMat = pd.DataFrame(StandardScaler().fit_transform(values), index=countries, columns=varHeaders) #standarization of values --> z = (x - u) / s
# valuesCov = np.cov(valuesStd.T) #we need transposed matrix as numpy calculates the array as X = [x_1, x_2, ... x_N]^T

valuesStd = valuesStdMat.values

ojaRule = Oja(valuesStd.shape[1])

infUnW = ojaRule.trainRule(valuesStd, 5000)

print(ojaRule.w)

#pca calculation
pca = PCA().fit(valuesStd)

pca_factory = PCA(n_components=5) #0.96 covered
Y = pca_factory.fit_transform(valuesStd)

components = pca_factory.fit(valuesStd)

print(components.components_[0]) #this shows the influence of every variable in the first component

variables = ["Area", "GDP", "Inflation", "LE", "Military", "PG", "Unemployment"]

# df = pd.DataFrame(valuesStd, columns=variables)
# boxplot = df.boxplot(column=variables)
# plt.savefig('Boxplot')
# plt.show()




infUnW = np.array(infUnW)
inflation = valuesStd[:,1]
unemployment = valuesStd[:,3]
inflationW = []
unemploymentW = []
for infVal in infUnW:
    inflationW.append(infVal[0])
    unemploymentW.append(infVal[1])


x = np.array(range(valuesStd.shape[1]))

printingW = ojaRule.w
# fig, ax = plt.subplots()
if np.linalg.norm(ojaRule.w - components.components_[0]) > np.linalg.norm((ojaRule.w * -1) - components.components_[0]):
    printingW = ojaRule.w * -1



# plt.scatter(x, printingW)
# plt.scatter(x, components.components_[0])
# plt.bar(x, printingW - components.components_[0], align='center', alpha=0.5)
# plt.fill_between(x, printingW, components.components_[0], color='grey', alpha=0.3)

print(printingW -components.components_[0])

ymin = min(printingW)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(x,printingW )
ax.scatter(x,components.components_[0])
ax.bar(x,printingW -components.components_[0])

for i in range(valuesStd.shape[1]):
    plt.text(i, ymin - 0.2, variables[i])


plt.savefig('DiferenceEtaFixed')

plt.show()


