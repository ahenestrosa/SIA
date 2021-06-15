import numpy as np
import fonts as ft
import random as rd
from PerceptronMultilayer import PerceptronMultilayer

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



def multipleSamplePercentaje(fontBitmap):
    sampleP = [0.25, 0.5 , 0.75]
    fontModified = []
    for i in sampleP:
        fontModified.clear()
        print(f'{i} of dataset')
        font = (rd.sample(fontBitmap, int(len(fontBitmap)*i)))
        for i in range(len(font)):
            print("\n~~~ Original ~~~\n")
            printSymbol(font[i].reshape(7,5))
        for i in range(len(font)):
            fontModified.append(addNoise(font[i].reshape(7,5), 0.10))
            print("\n~~~ Noise ~~~ \n")
            printSymbol(fontModified[i].reshape(7,5))



multipleSamplePercentaje(ft.font1bitmap)

font = (rd.sample(ft.font1bitmap, int(len(ft.font1bitmap)*0.25)))
