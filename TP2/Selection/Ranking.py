
import random



def select(characters, K):

    total_ranking = 0
    selection = []
    i = 1
    character_size = len(characters)

    while i <= character_size:
        total_ranking += i
        i += 1
    characters.sort(reverse=True)
    for i in range(K):
        random_num = random.uniform(0, 1)
        sum_rank = 0
        j = 0
        found = False
        while j < (character_size - 1) and not found:

            sum_rank += (character_size - j)/ total_ranking #pseudo fitness calculation
            if j == 0:
                if random_num < sum_rank:
                    selection.append(characters[j])
                    found = True
            else:
                if random_num >= sum_rank and random_num < (sum_rank + ((character_size - (j + 1)) / total_ranking)):
                    selection.append(characters[j + 1])
                    found = True
            j += 1

    return selection
