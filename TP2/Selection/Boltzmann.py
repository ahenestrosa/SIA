import math
import random


T0_CONST = 3
TC_CONST = 1.0
K_CONST = 0.1

def select(characters, K, t, t0_temp, tc_temp, k_temp):
    total_boltzman = 0
    selection = []
    for char in characters:
        total_boltzman += calculate_pseudo(char, t, t0_temp,tc_temp,k_temp)

    for i in range(K):
        random_num = random.uniform(0,1)
        sum_boltz = 0
        j = 0
        found = False
        while j < (len(characters) - 1) and not found:
            sum_boltz += (calculate_pseudo(characters[j], t, t0_temp, tc_temp, k_temp)/ total_boltzman)
            if j == 0:
                if random_num < sum_boltz:
                    selection.append(characters[j])
                    found = True
                elif random_num >= sum_boltz and random_num < (sum_boltz + calculate_pseudo(characters[j+1], t, t0_temp, tc_temp, k_temp)/ total_boltzman):
                    selection.append(characters[j + 1])
                    found = True
            else:
                if random_num >= sum_boltz and random_num < (sum_boltz + calculate_pseudo(characters[j+1], t, t0_temp, tc_temp, k_temp)/ total_boltzman):
                    selection.append(characters[j + 1])
                    found = True
            j += 1
    return selection


def calculate_pseudo(char, t, t0_temp=T0_CONST, tc_temp=TC_CONST, k_temp=K_CONST):
    return math.exp(char.fitness / temperature(t, t0_temp, tc_temp, k_temp))


def temperature(t, t0_temp, tc_temp, k_temp):
    return tc_temp + (t0_temp - tc_temp) * math.exp(-k_temp * t)