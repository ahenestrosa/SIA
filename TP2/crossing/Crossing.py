from Utilities import Constants
from Character import Character
from random import randrange, uniform
import math

class Crossing:

    @classmethod
    def onePointCrossing(cls, parent1, parent2):
        gn = randrange(Constants.GENES_SIZE)
        gen = Constants.GENES_LIST[gn]

        child1Height = parent1.height
        child2Height = parent2.height
        child1Items = parent1.items.copy()
        child2Items = parent2.items.copy()

        if gen == Constants.GEN_HEIGHT:
            child1Height = parent2.height
            child2Height = parent1.height
        else:
            child1Items[gen] = parent2.items[gen]
            child2Items[gen] = parent1.items[gen]
            
        child1 = Character(parent1.pj_clas, child1Height, child1Items, parent1.characterId + "-1")
        child2 = Character(parent1.pj_clas, child2Height, child2Items, parent2.characterId + "-2")
        return (child1, child2)

    @classmethod
    def twoPointCrossing(cls, parent1, parent2):
        g1 = randrange(Constants.GENES_SIZE)
        g2 = randrange(Constants.GENES_SIZE)
        if g1 > g2:
            tmp = g1
            g1 = g2
            g2 = tmp
        
        genes1List = parent1.get_genes()
        genes2List = parent2.get_genes()

        for i in range(g1, g2+1):
            tmp = genes1List[i]
            genes1List[i] = genes2List[i]
            genes2List[i] = tmp

        
        child1Items = {
            Constants.BOTA:    genes1List[1],
            Constants.ARMA:    genes1List[2],
            Constants.CASCO:   genes1List[3],
            Constants.GUANTE:  genes1List[4],
            Constants.PECHERA: genes1List[5]
        }
        child1 = Character(parent1.pj_clas, genes1List[0], child1Items, parent1.characterId + "-1")

        child2Items = {
            Constants.BOTA:    genes2List[1],
            Constants.ARMA:    genes2List[2],
            Constants.CASCO:   genes2List[3],
            Constants.GUANTE:  genes2List[4],
            Constants.PECHERA: genes2List[5]
        }
        child2 = Character(parent1.pj_clas, genes2List[0], child2Items, parent2.characterId + "-2")

        return (child1, child2)

    @classmethod
    def anularCrossing(cls, parent1, parent2):
        p = randrange(Constants.GENES_SIZE)
        l = randrange(math.ceil(Constants.GENES_SIZE/2))
        
        genes1List = parent1.get_genes()
        genes2List = parent2.get_genes()

        while(l > 0):
            tmp = genes1List[p]
            genes1List[p] = genes2List[p]
            genes2List[p] = tmp
            p = (p+1) % Constants.GENES_SIZE
            l -= 1

        child1Items = {
            Constants.BOTA:    genes1List[1],
            Constants.ARMA:    genes1List[2],
            Constants.CASCO:   genes1List[3],
            Constants.GUANTE:  genes1List[4],
            Constants.PECHERA: genes1List[5]
        }
        child1 = Character(parent1.pj_clas, genes1List[0], child1Items, parent1.characterId + "-1")

        child2Items = {
            Constants.BOTA:    genes2List[1],
            Constants.ARMA:    genes2List[2],
            Constants.CASCO:   genes2List[3],
            Constants.GUANTE:  genes2List[4],
            Constants.PECHERA: genes2List[5]
        }
        child2 = Character(parent1.pj_clas, genes2List[0], child2Items, parent2.characterId + "-2")

        return (child1, child2)



    @classmethod
    def unifromCrossing(cls, parent1, parent2):
        genes1List = parent1.get_genes()
        genes2List = parent2.get_genes()
        
        for i in range(0, Constants.GENES_SIZE):
            swap = randrange(2)
            if swap == 0:
                tmp = genes1List[i]
                genes1List[i] = genes2List[i]
                genes2List[i] = tmp

        child1Items = {
            Constants.BOTA:    genes1List[1],
            Constants.ARMA:    genes1List[2],
            Constants.CASCO:   genes1List[3],
            Constants.GUANTE:  genes1List[4],
            Constants.PECHERA: genes1List[5]
        }
        child1 = Character(parent1.pj_clas, genes1List[0], child1Items, parent1.characterId + "-1")

        child2Items = {
            Constants.BOTA:    genes2List[1],
            Constants.ARMA:    genes2List[2],
            Constants.CASCO:   genes2List[3],
            Constants.GUANTE:  genes2List[4],
            Constants.PECHERA: genes2List[5]
        }
        child2 = Character(parent1.pj_clas, genes2List[0], child2Items, parent2.characterId + "-2")

        return (child1, child2)