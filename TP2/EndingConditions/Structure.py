import math

DELTA_HEIGHT = 0.1
DELTA_ATTACK_DEFENSE = 1.0
DELTA_FITNESS = 0.5
POB_PROP = 1/4
def is_finished(characters_gen, generations):
    gen = 0
    if len(characters_gen) < generations:
        return False

    while gen < generations - 1:
        j = 0
        counter = 0
        if gen == 0:
            characters_gen[gen].sort()
        else:
            characters_gen[gen + 1].sort()

        while j < len(characters_gen[gen]):
            if abs(characters_gen[gen][j].height - characters_gen[gen + 1][j].height) > DELTA_HEIGHT or abs(characters_gen[gen][j].attack - characters_gen[gen + 1][j].attack) > DELTA_ATTACK_DEFENSE or abs(characters_gen[gen][j].defense - characters_gen[gen + 1][j].defense) > DELTA_ATTACK_DEFENSE or abs(characters_gen[gen][j].fitness - characters_gen[gen + 1][j].fitness) > DELTA_FITNESS:
                counter += 1
            j += 1
        if counter < len(characters_gen[gen]) * POB_PROP:
            return False
        gen += 1


    if counter < len(characters_gen[0]) * POB_PROP * (generations - 1):
        return False
    else:
        return True
