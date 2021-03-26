from Character import Character
from Utilities import Utilities
from Utilities import Constants




boots = Utilities.itemParse(Constants.BOTAS_PATH)
weapons = Utilities.itemParse(Constants.ARMAS_PATH)
armor = Utilities.itemParse(Constants.PECHERAS_PATH)
gloves = Utilities.itemParse(Constants.GUANTES_PATH)
helmet = Utilities.itemParse(Constants.CASCOS_PATH)


items = [boots['5'], weapons['1000'], armor['3500'], gloves['322'], helmet['4333']]


char = Character(Constants.GUERRERO, 1.8, items)

char.calculate_stats()

print(char.fitness())
