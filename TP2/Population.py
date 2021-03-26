from random import randrange, uniform
from Utilities import Constants

class Population:
    populationSize = 0
    characters = []
    itemsInformation = {}
    def __init__(self, populationSize, itemsInformation):
        self.populationSize = populationSize
        self.itemsInformation = itemsInformation

    
    def generateRandomPopulation(self):
        for i in range(0, self.populationSize):
            #Calculate random pj class
            pjClass =  Constants.PJ_CLASSES[randrange(4)]
            #Calculate random height
            height = uniform(Constants.MIN_HEIGHT, Constants.MAX_HEIGHT)
            #Calculate 5 random items
            itemList = []
            for i in range(0, 5):
                currentItem = Constants.ITEMS_LIST[0]
                randomItemNumber = randrange(Constants.ITEMS_SIZE)
                newItem = itemsInformation[currentItem][randomItemNumber]
                itemList.append(newItem)

            self.characters.append(pjClass, height, itemList)                
