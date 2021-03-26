from Character import Character
from Utilities import Utilities
from Utilities import Constants
from Selection import Elite
from Selection import Roulette


boots = Utilities.itemParse(Constants.BOTAS_PATH)
weapons = Utilities.itemParse(Constants.ARMAS_PATH)
armor = Utilities.itemParse(Constants.PECHERAS_PATH)
gloves = Utilities.itemParse(Constants.GUANTES_PATH)
helmets = Utilities.itemParse(Constants.CASCOS_PATH)


# items = [boots['5'], weapons['1000'], armor['3500'], gloves['322'], helmets['4333']]


g0 = Utilities.generateRandom(10,weapons, boots, gloves, armor, helmets)


g1 = Roulette.select(g0, 5)




print(g0)