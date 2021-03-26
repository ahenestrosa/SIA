import random


def select(characters, K, M):
    selected = []
    for i in range(K):
        candidates = []
        for j in range(M):
            random_int= random.randint(0, len(characters) - 1)
            candidates.append(characters[random_int])
        candidates.sort(reverse=True)
        selected.append(candidates[0])
    return selected