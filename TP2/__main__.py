from Character import Character
from Utilities import Utilities
from Utilities import Constants
from Population import Population




boots = Utilities.itemParse(Constants.BOTAS_PATH)
weapons = Utilities.itemParse(Constants.ARMAS_PATH)
armor = Utilities.itemParse(Constants.PECHERAS_PATH)
gloves = Utilities.itemParse(Constants.GUANTES_PATH)
helmet = Utilities.itemParse(Constants.CASCOS_PATH)

items_information = {
    Constants.BOTA: boots,
    Constants.ARMA: weapons,
    Constants.CASCO: helmet,
    Constants.GUANTE: glove,
    Constants.PECHERA: armor
}

pop = Population(30, items_information)
pop.generateRandomPopulation()

