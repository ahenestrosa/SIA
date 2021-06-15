
import numpy as np

def mapToBlack(digit):
    bitmap = np.zeros((7,5))
    i = 0
    for i in range(len(digit)):
        for j in range(len(digit[i])):
            elem = digit[i][j]
            r = 1
            if elem >= 0.5:
                r = 0
            bitmap[i][j] = r

    return bitmap