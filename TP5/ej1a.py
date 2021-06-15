#!/bin/python3

import numpy as np
import fonts as ft
from copy import deepcopy
import random as rd
from PerceptronMultilayer import PerceptronMultilayer
from utils import printMatrix, arrayTo2DMatrix


#sets the sample taken to train the multilayer
samplePer = 1

middlelayer = [2]

activationSearch = (len(middlelayer) + 2) // 2

font1sample = (rd.sample(ft.font1bitmap, int(len(ft.font1bitmap)*samplePer))) #formats the input and takes a random sample from the fonts



multiLayerPerceptron = PerceptronMultilayer(35,35,middlelayer, 'tanh', 0.01,costFunction='entropic', momentum=0.9, adaptative=(0.0001, 0.00001))
multiLayerPerceptron.train(10, 500, font1sample, font1sample, verbose=True)


for letter in font1sample:
    print('############################################################')
    r, a, v = multiLayerPerceptron.calculateOutput(letter)
    print("Expected: " )
    printMatrix(arrayTo2DMatrix(letter,5))
    print("Actual:")
    printMatrix(arrayTo2DMatrix(r,5))

    print(a[activationSearch])
    # print("Classified: " +  str(classify(r[0,0])))
    # print()



