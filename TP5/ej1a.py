#!/bin/python3

import numpy as np
import fonts as ft
from copy import deepcopy
import random as rd
from PerceptronMultilayer import PerceptronMultilayer


#sets the sample taken to train the multilayer
samplePer = 6/32





font1sample = (rd.sample(ft.font1bitmap, int(len(ft.font1bitmap)*samplePer))) #formats the input and takes a random sample from the fonts



multiLayerPerceptron = PerceptronMultilayer(35,35,[8,4,2], 'tanh', 0.01)
multiLayerPerceptron.train(0.001, 2000, font1sample, font1sample, verbose=True)




