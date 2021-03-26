from Character import Character
from Utilities import Utilities
from Utilities import Constants
from Population import Population
from Selection import Elite
from Selection import Roulette
from Selection import Ranking
from Selection import Universal
import json


items_information = {
    Constants.BOTA:    Utilities.itemParse(Constants.BOTAS_PATH),
    Constants.ARMA:    Utilities.itemParse(Constants.ARMAS_PATH),
    Constants.CASCO:   Utilities.itemParse(Constants.CASCOS_PATH),
    Constants.GUANTE:  Utilities.itemParse(Constants.GUANTES_PATH),
    Constants.PECHERA: Utilities.itemParse(Constants.PECHERAS_PATH)
}

pop = Population(5, items_information)
pop.generateRandomPopulation()

for c in pop.characters:
    print(c)
    print()



# with open('config.json') as config:
#     data = json.load(config)

# crossing = data['crossing']
# mutation = data['mutation']
# selector = data['selector']
# implementation = data["implementation"]
# stop = data["stop"]
# character = data["character"]
# pm = data["pm"]

