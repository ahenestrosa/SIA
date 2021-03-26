import numpy as np
import math
from random import randint
def select(characters, K):
    selection = []
    characters.sort(reverse=True)
    i = 0
    for char in characters:
        n = math.ceil((K - i)/len(characters))
        for t in range(n):
            selection.append(char)
        i += 1

    return selection