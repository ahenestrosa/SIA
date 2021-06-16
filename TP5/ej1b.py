import numpy as np
import fonts as ft
import random as rd
from PerceptronMultilayer import PerceptronMultilayer
import utils 
import matplotlib.pyplot as plt


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


def showColorMap(original, modified, output, filename):
    n = 7
    digit_width = 5
    digit_height = 7
    figure = np.ones((digit_height * n, digit_width * 3))

    for i, yi in enumerate(range(n)):
        figure[i * digit_height: (i + 1) * digit_height,
            0 * digit_width: (0 + 1) * digit_width] = 1- original[i].reshape(digit_height, digit_width)
        figure[i * digit_height: (i + 1) * digit_height,
            1 * digit_width: (1 + 1) * digit_width] = 1-modified[i].reshape(digit_height, digit_width)
        figure[i * digit_height: (i + 1) * digit_height,
            2 * digit_width: (2 + 1) * digit_width] = 1-output[i].reshape(digit_height, digit_width)
        

    plt.figure(figsize=(10, 10))
    plt.imshow(figure , cmap='Greys_r')

    xline = np.linspace(-0.5, digit_width*3 - 0.5)
    for i in range(1, n):
        plt.plot(xline, np.array([-0.5+digit_height*i for t in range(len(xline))]), color='red', linewidth=3)

    yline = np.linspace(-0.5, digit_height*n - 0.5)
    for i in range(1, 3):
        plt.plot(np.array([-0.5+digit_width*i for t in range(len(yline))]) ,yline, color='red', linewidth=3)


    # plt.show()
    plt.savefig(filename + '.png', bbox_inches='tight')



def multipleSamplePercentaje(fontBitmap,pm):
    sampleP = [0.25, 0.5 , 0.75, 1]
    fontModified = []
    for i in sampleP:
        fontModified.clear()
        print(f'{i} of dataset')
        font = fontBitmap[0:int(len(fontBitmap)*i)]
                # for k in range(len(font)):
        #     print("\n~~~ Original ~~~\n")
        #     printSymbol(font[k].reshape(7,5))
        for p in range(len(font)):
            fontModified.append(addNoise(font[p].reshape(7,5), pm))
            # print("\n~~~ Noise ~~~ \n")
            # printSymbol(fontModified[p].reshape(7,5))
        multiLayerPerceptron = PerceptronMultilayer(35,35,[12], 'tanh', 0.01,costFunction='entropic', momentum=0.9, adaptative=(0.0001, 0.00001))
        multiLayerPerceptron.train(10, 500, fontModified, font)
        outputs = []
        for i in range(len(fontModified)):
            print('############################################################')
            r, a, v = multiLayerPerceptron.calculateOutput(font[i])
            print("Original: " )
            utils.printMatrix(utils.arrayTo2DMatrix(font[i],5))
            print("Noisy:")
            utils.printMatrix(utils.arrayTo2DMatrix(fontModified[i],5))
            print("Autoencoder Output: ")
            utils.printMatrix(utils.arrayTo2DMatrix(r,5))
            outputs.append(r)
        showColorMap(font, fontModified, outputs, "Dae_" + str(pm) + "_" + str(i))

# 10% noise
multipleSamplePercentaje(ft.font2bitmap,0.10)

# 20% noise 
multipleSamplePercentaje(ft.font2bitmap,0.20)

# 30% noise 
multipleSamplePercentaje(ft.font2bitmap,0.30)
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
