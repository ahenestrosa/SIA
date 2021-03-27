from random import randrange, uniform
from Utilities import Constants
from Character import Character

import math
from functools import partial

class Population:
    populationSize = 0
    characters = []
    itemsInformation = {}
    extraSelectionArgument = None
    iteration = 0
    def __init__(self, populationSize, itemsInformation, crossing, mutation, selection, extraArgument=None):
        self.populationSize = populationSize
        self.itemsInformation = itemsInformation
        self.crossing = crossing
        self.mutation = mutation
        self.selection = selection
        self.extraSelectionArgument = extraArgument

    
    def generateRandomPopulation(self):
        for i in range(0, self.populationSize):
            #Calculate random pj class
            pjClass =  Constants.PJ_CLASSES[randrange(4)]
            #Calculate random height
            height = uniform(Constants.MIN_HEIGHT, Constants.MAX_HEIGHT)
            #Calculate 5 random items
            items = {}
            for j in range(0, 5):
                currentItem = Constants.ITEMS_LIST[j]
                randomItemNumber = randrange(Constants.ITEMS_SIZE)
                newItem = self.itemsInformation[currentItem][randomItemNumber]
                items[currentItem] = newItem

            self.characters.append(Character(pjClass, height, items, str(i)))

    
    def performSelection(self):
        allCharacters = self.performCrossing()
        #TODO: Add fill all and fill other
        if self.extraSelectionArgument == None:
            self.characters = self.selection(allCharacters, self.populationSize)
        elif self.extraSelectionArgument == "it":
            self.characters = self.selection(allCharacters, self.populationSize, self.iteration)
        else:
            self.characters = self.selection(allCharacters, self.populationSize, self.extraSelectionArgument)
    
        self.iteration += 1

    def performCrossing(self):
        allCharacters = []
        for i in range(0, math.floor(self.populationSize/2), 2):
            p1 = self.characters[i]
            p2 = self.characters[i+1]
            (c1, c2) = self.crossing(p1, p2)
            #TODO: Perform mutations over c1 and c2
            allCharacters.append(p1)
            allCharacters.append(p2)
            allCharacters.append(c1)
            allCharacters.append(c2)
        return allCharacters


    def getFitnessOfPopulation(self):
        averageFitness = 0
        minFitness = -1
        for i in range(0, self.populationSize):
            f = self.characters[i].fitness
            averageFitness += f
            if minFitness == -1 or minFitness > f:
                minFitness = f
        averageFitness = averageFitness / self.populationSize
        return (averageFitness, minFitness)



