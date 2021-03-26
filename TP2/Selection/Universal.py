import math
import random




def select(characters, K):
    selection = []
    total_fitness = 0
    for char in characters:
        total_fitness += char.fitness
    for i in range(K):
        random_num = (random.uniform(0,1) + i) / K
        sum_fit = 0
        j = 0
        found = False
        while j < (len(characters) - 1) and not found:
            sum_fit += (characters[j].fitness / total_fitness)
            if j == 0:
                if random_num < sum_fit:
                    selection.append(characters[j])
                    found = True
            else:
                if random_num >= sum_fit and random_num < (sum_fit + (characters[j+1].fitness/ total_fitness)):
                    selection.append(characters[j + 1])
                    found = True
            j += 1
    return selection