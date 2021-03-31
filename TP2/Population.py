from random import randrange, uniform
from Utilities import Constants
from Character import Character
from EndingConditions.EndingConditions import EndingConditions
import matplotlib.pyplot as plt
import math
from functools import partial
import time
import numpy as np


class Population:
    populationSize = 0
    characters = []
    itemsInformation = {}
    extraSelectionArgument = None
    iteration = 0
    iterationTime = 0
    charactersGeneration = []
    def __init__(self, populationClass, populationSize, itemsInformation, crossing, mutation, mutationProb, selection, selectionChilds, fillMethod, extraArgument=None):
        self.populationClass = populationClass
        self.populationSize = populationSize
        self.itemsInformation = itemsInformation
        self.crossing = crossing
        self.mutation = mutation
        self.mutationProb = mutationProb
        self.selection = selection
        self.selectionChilds = selectionChilds
        self.fillMethod = fillMethod
        self.extraSelectionArgument = extraArgument

    
    def generateRandomPopulation(self):
        for i in range(0, self.populationSize):
            #Calculate random height
            height = uniform(Constants.MIN_HEIGHT, Constants.MAX_HEIGHT)
            #Calculate 5 random items
            items = {}
            for j in range(0, 5):
                currentItem = Constants.ITEMS_LIST[j]
                randomItemNumber = randrange(Constants.ITEMS_SIZE)
                newItem = self.itemsInformation[currentItem][randomItemNumber]
                items[currentItem] = newItem

            self.characters.append(Character(self.populationClass, height, items, str(i)))

    def performLifeCycle(self, endingCondition, endingParameters):
        ended = False
        self.iterationTime = time.time()

        #Plot
        plt.xlabel("Generation")
        plt.ylabel("Fitness")
        while not ended:
            (avgF, minF) = self.getFitnessOfPopulation()
            print(str(self.iteration) +  " - Avg: " + str(avgF) + " Min: " + str(minF))
            plt.scatter(self.iteration,avgF, c='red', label='Avg')
            plt.scatter(self.iteration,minF, c='green', label='Min Fitness')
            plt.pause(0.05)
            self.performSelection()
            self.iteration +=1
            ended = self.getEndingCondition(endingCondition, endingParameters)
            
        plt.show()
    

    def getEndingCondition(self, endingCondition, params):
        if endingCondition == "ACC_SOL":
            return EndingConditions.accSolutionEnding(self.characters, params[0])
        elif endingCondition == "CONTENT":
            self.pushToQueue(params[0], self.characters)
            if len(self.charactersGeneration) > 1:
                return EndingConditions.contentEnding(self.charactersGeneration, params[0], params[1])
            return False
        elif endingCondition == "GEN_AMMOUNT":
            return EndingConditions.generationsAmmountEnding(self.iteration, params[0])
        elif endingCondition == "STRUCTURE":
            self.pushToQueue(params[0], self.characters)
            if len(self.charactersGeneration) > 1:
                return EndingConditions.structureEnding(self.charactersGeneration, self.iteration, params[0], params[1], params[2], params[3], params[4])
            return False
        elif endingCondition == "TIME":
            return EndingConditions.timeEnding(time.time() -self.iterationTime, params[0])

    def pushToQueue(self, generations, characters):
        if len(self.charactersGeneration) == generations:
            del self.charactersGeneration[0]

        self.charactersGeneration.append(characters)


    def performSelection(self):
        childCharacters = self.performCrossing()

        charactersToSelect = []
        selectedCharacters = None
        selectionSize = None
        newGenerationCharacters = []

        if self.fillMethod == "FILL_ALL":
            charactersToSelect.extend(self.characters)
            charactersToSelect.extend(childCharacters)
            selectionSize = self.populationSize
        elif self.fillMethod == "FILL_PARENT":
            if len(childCharacters) > self.populationSize:
                charactersToSelect.extend(childCharacters)
                selectionSize = self.populationSize
            else:
                charactersToSelect.extend(self.characters)
                selectionSize = self.populationSize-len(childCharacters)
                newGenerationCharacters.extend(childCharacters)

        
        if self.extraSelectionArgument == None:
            selectedCharacters = self.selection(charactersToSelect, selectionSize)
        elif self.extraSelectionArgument == "it":
            selectedCharacters = self.selection(charactersToSelect, selectionSize, self.iteration)
        else:
            selectedCharacters = self.selection(charactersToSelect, selectionSize, self.extraSelectionArgument)

        newGenerationCharacters.extend(selectedCharacters)
        self.characters = newGenerationCharacters



    def performCrossing(self):
        childCharacters = []
        for i in range(0, math.floor(self.selectionChilds/2)):
            p1 = self.characters[randrange(self.populationSize)]
            p2 = self.characters[randrange(self.populationSize)]
            (c1, c2) = self.crossing(p1, p2)
            c1 = self.mutation(self.mutationProb, c1, self.itemsInformation)
            c2 = self.mutation(self.mutationProb, c2, self.itemsInformation)
            childCharacters.append(c1)
            childCharacters.append(c2)
        return childCharacters


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



