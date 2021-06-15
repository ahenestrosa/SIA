import numpy as np
import fonts as ft
import random as rd
from PerceptronMultilayer import PerceptronMultilayer
import utils 

def classify(num):
    if num > 0:
        return 1
    return -1

def addNoise(symbol, pm):
    modified = []
    for i in range(symbol.shape[0]):
        for j in range(symbol.shape[1]):    
            m = rd.uniform(0, 1)
            if m <= pm:
                modified.append(symbol.item((i, j)) * -1)
            else:
                modified.append(symbol.item((i, j)))

    return np.reshape(modified, (35,))

def printSymbol(symbol):
    for i in range(symbol.shape[0]):
        for j in range(symbol.shape[1]):
            print('%s' % '*' if symbol.item((i, j)) == 1 else ' ', end='') 
        print()





def multipleSamplePercentaje(fontBitmap,pm):
    sampleP = [0.25, 0.5 , 0.75]
    fontModified = []
    for i in sampleP:
        fontModified.clear()
        print(f'{i} of dataset')
        font = (rd.sample(fontBitmap, int(len(fontBitmap)*i)))
        # for k in range(len(font)):
        #     print("\n~~~ Original ~~~\n")
        #     printSymbol(font[k].reshape(7,5))
        for p in range(len(font)):
            fontModified.append(addNoise(font[p].reshape(7,5), pm))
            # print("\n~~~ Noise ~~~ \n")
            # printSymbol(fontModified[p].reshape(7,5))
        multiLayerPerceptron = PerceptronMultilayer(35,35,[12], 'tanh', 0.01,costFunction='entropic', momentum=0.9, adaptative=(0.0001, 0.00001))
        multiLayerPerceptron.train(10, 500, fontModified, font)
        for i in range(len(fontModified)):
            print('############################################################')
            r, a, v = multiLayerPerceptron.calculateOutput(font[i])
            print("Original: " )
            utils.printMatrix(utils.arrayTo2DMatrix(font[i],5))
            print("Noisy:")
            utils.printMatrix(utils.arrayTo2DMatrix(fontModified[i],5))
            print("Autoencoder Output: ")
            utils.printMatrix(utils.arrayTo2DMatrix(r,5))


# 10% noise
multipleSamplePercentaje(ft.font1bitmap,0.10)

# 20% noise 
multipleSamplePercentaje(ft.font1bitmap,0.20)

# 30% noise 
multipleSamplePercentaje(ft.font1bitmap,0.30)
"""

font = (rd.sample(ft.font1bitmap, int(len(ft.font1bitmap)*0.5)))
fontModified = []
for i in range(len(font)):
    fontModified.append(addNoise(font[i].reshape(7,5), 0.30))
    # print("\n~~~ Noise ~~~ \n")
    # printSymbol(fontModified[i].reshape(7,5))
testInput = fontModified[rd.randint(0,len(fontModified))]


multiLayerPerceptron = PerceptronMultilayer(35,35,[24,12,24], 'tanh', 0.01,costFunction='entropic', momentum=0.9, adaptative=(0.0001, 0.00001))
multiLayerPerceptron.train(10, 500, fontModified, font)


for i in range(len(fontModified)):
    print('############################################################')
    r, a, v = multiLayerPerceptron.calculateOutput(font[i])
    print("Original: " )
    utils.printMatrix(utils.arrayTo2DMatrix(font[i],5))
    print("Noisy:")
    utils.printMatrix(utils.arrayTo2DMatrix(fontModified[i],5))
    print("Autoencoder Output: ")
    utils.printMatrix(utils.arrayTo2DMatrix(r,5))

"""
