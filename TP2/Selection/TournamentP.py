import random

def select(characters, K, threshold):
    selected = []

    for i in range(K):
        candidates = []
        for j in range(2):
            random_int = random.randint(0, len(characters) - 1)
            candidates.append(characters[random_int])
        r = random.uniform(0, 1)
        candidates.sort(reverse=True)
        if(r < threshold):
            selected.append(candidates[0])
        else:
            selected.append(candidates[1])

    return selected