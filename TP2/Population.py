from random import randrange, uniform, shuffle
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
    def __init__(self, populationClass, populationSize, itemsInformation, crossing, mutation, mutationProb, selectionMethod1, selectionMethod2, selectionMethod3, selectionMethod4, selectorA, selectorB,selectionChilds, fillMethod):
        self.populationClass = populationClass
        self.populationSize = populationSize
        self.itemsInformation = itemsInformation
        self.crossing = crossing
        self.mutation = mutation
        self.mutationProb = mutationProb
        self.selectionMethod1= selectionMethod1
        self.selectionMethod2= selectionMethod2
        self.selectionMethod3= selectionMethod3
        self.selectionMethod4= selectionMethod4
        self.selectorA = selectorA
        self.selectorB = selectorB
        self.selectionChilds = selectionChilds
        self.fillMethod = fillMethod

    
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

    def performSelection(self):
        childCharacters = self.performCrossing()

        charactersToSelect = []
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

        selectedCharacters3 = []
        selectedCharacters4 = []
        selectionSizeMethod3 = math.floor(selectionSize * self.selectorB)
        selectionSizeMethod4 = math.ceil(selectionSize * (1 - self.selectorB))

        if selectionSizeMethod3 > 0:
            if self.selectionMethod3[1] == None:
                selectedCharacters3 = self.selectionMethod3[0](charactersToSelect.copy(), selectionSizeMethod3)
            elif self.selectionMethod3[1] == "it":
                selectedCharacters3 = self.selectionMethod3[0](charactersToSelect.copy(), selectionSizeMethod3, self.iteration)
            else:
                selectedCharacters3 = self.selectionMethod3[0](charactersToSelect.copy(), selectionSizeMethod3, self.selectionMethod3[1])

        if selectionSizeMethod4 > 0:
            if self.selectionMethod4[1] == None:
                selectedCharacters4 = self.selectionMethod4[0](charactersToSelect.copy(), selectionSizeMethod4)
            elif self.selectionMethod4[1] == "it":
                selectedCharacters4 = self.selectionMethod4[0](charactersToSelect.copy(), selectionSizeMethod4, self.iteration)
            else:
                selectedCharacters4 = self.selectionMethod4[0]=(charactersToSelect.copy(), selectionSizeMethod4, self.selectionMethod4[1])

    
        newGenerationCharacters.extend(selectedCharacters3)
        newGenerationCharacters.extend(selectedCharacters4)
        self.characters = newGenerationCharacters



    def performCrossing(self):
        childCharacters = []

        parentsToCross = []
        selectedParents1 = []
        selectedParents2 = []
        selectionSizeMethod1 = math.floor(self.selectionChilds * self.selectorA)
        selectionSizeMethod2 = math.ceil(self.selectionChilds * (1 - self.selectorA))

        if selectionSizeMethod1 > 0:
            if self.selectionMethod1[1] == None:
                selectedParents1 = self.selectionMethod1[0](self.characters.copy(), selectionSizeMethod1)
            elif self.selectionMethod1[1] == "it":
                selectedParents1 = self.selectionMethod1[0](self.characters.copy(), selectionSizeMethod1, self.iteration)
            else:
                selectedParents1 = self.selectionMethod1[0](self.characters.copy(), selectionSizeMethod1, self.selectionMethod1[1])

        if selectionSizeMethod2 > 0:
            if self.selectionMethod2[1] == None:
                selectedParents2 = self.selectionMethod2[0](self.characters.copy(), selectionSizeMethod2)
            elif self.selectionMethod2[1] == "it":
                selectedParents2 = self.selectionMethod2[0](self.characters.copy(), selectionSizeMethod2, self.iteration)
            else:
                selectedParents2 = self.selectionMethod2[0](self.characters.copy(), selectionSizeMethod2, self.selectionMethod2[1])

        parentsToCross.extend(selectedParents1)
        parentsToCross.extend(selectedParents2)
        shuffle(parentsToCross)

        for i in range(0, math.floor(self.selectionChilds/2)):
            p1 = parentsToCross[i]
            p2 = parentsToCross[i+1]
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

    def pushToQueue(self, generations, characters):
        if len(self.charactersGeneration) == generations:
            del self.charactersGeneration[0]

        self.charactersGeneration.append(characters)

