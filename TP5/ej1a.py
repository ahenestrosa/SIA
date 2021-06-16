#!/bin/python3

import numpy as np
import fonts as ft
from copy import deepcopy
import random as rd
from PerceptronMultilayer import PerceptronMultilayer
from utils import printMatrix, arrayTo2DMatrix, outputFromLayerReshape
import matplotlib.pyplot as plt
from scipy.stats import norm



#sets the sample taken to train the multilayer
samplePer = 0.125

middlelayer = [16,2,16]

activationSearch = (len(middlelayer) + 1) // 2

# font2sample = (rd.sample(ft.font2bitmap, int(len(ft.font2bitmap)*samplePer))) #formats the input and takes a random sample from the fonts
font2sample = ft.font2bitmap[1:5]

multiLayerPerceptron = PerceptronMultilayer(35,35,middlelayer, 'tanh', 0.01,costFunction='entropic', momentum=None, adaptative=(0.0001, 0.00001))

multiLayerPerceptron.train(1, 500, font2sample, font2sample, verbose=True)


for letter in font2sample:
    print('############################################################')
    r, a, v = multiLayerPerceptron.calculateOutput(letter)
    print("Expected: " )
    printMatrix(arrayTo2DMatrix(letter,5))
    print("Actual:")
    printMatrix(arrayTo2DMatrix(r,5))

    print(a[activationSearch])
    # print("Classified: " +  str(classify(r[0,0])))
    # print()





### Representacion de la capa latente

x_test_encoded = np.zeros((len(font2sample), 2))
i = 0
for sample in font2sample:
    output = multiLayerPerceptron.forwardPropagateFromToLayer(sample, 0, activationSearch)
    x_test_encoded[i] = output.ravel()
    i += 1

plt.figure(figsize=(6, 6))
plt.scatter(x_test_encoded[:,0], x_test_encoded[:,1])
# for i, txt in enumerate(labels):
#     plt.annotate(txt, (x_test_encoded[i][0] + 0.05, x_test_encoded[i][1] + 0.05))
plt.show()


### Generacion moviendonos enel espacio latente

# print("Generation of Letter")

# for i in range(3):
#     oLay = [rd.random() * 2 - 1 for i in range(2)]
#     nLetter = multiLayerPerceptron.forwardPropagateFromLayer(oLay, activationSearch)
#     print(len(nLetter))
#     printMatrix(outputFromLayerReshape(nLetter, 5))



n = 10
digit_width = 5
digit_height = 7
figure = np.ones((digit_height * n, digit_width * n))
grid_x = np.linspace(-1, 1, n)
grid_y = np.linspace(-1, 1, n)

for i, yi in enumerate(grid_x):
    for j, xi in enumerate(grid_y):
        z_sample = np.array([[xi, yi]])
        x_decoded = multiLayerPerceptron.forwardPropagateFromLayer(z_sample, activationSearch)
        # print(fonts.printLetter(x_decoded[0]))
        digit = x_decoded.reshape(digit_height, digit_width)
        figure[i * digit_height: (i + 1) * digit_height,
               j * digit_width: (j + 1) * digit_width] = 1-digit

# figure[0][0] = 0

plt.figure(figsize=(10, 10))
plt.imshow(figure , cmap='Greys_r')

xline = np.linspace(-0.5, digit_width*n - 0.5)
for i in range(1, n):
    plt.plot(xline, np.array([-0.5+digit_height*i for t in range(len(xline))]), color='red', linewidth=3)

yline = np.linspace(-0.5, digit_height*n - 0.5)
for i in range(1, n):
    plt.plot(np.array([-0.5+digit_width*i for t in range(len(yline))]) ,yline, color='red', linewidth=3)


plt.show()