from Character import Character
from Utilities import Utilities
from Utilities import Constants
from Population import Population
from Selection import Elite
from Selection import Roulette
from Selection import Ranking
from Selection import Universal
from Selection import Boltzmann
from Selection import TournamentD
from Selection import TournamentP
from crossing.Crossing import Crossing
import json


items_information = {
    Constants.BOTA:    Utilities.itemParse(Constants.BOTAS_PATH),
    Constants.ARMA:    Utilities.itemParse(Constants.ARMAS_PATH),
    Constants.CASCO:   Utilities.itemParse(Constants.CASCOS_PATH),
    Constants.GUANTE:  Utilities.itemParse(Constants.GUANTES_PATH),
    Constants.PECHERA: Utilities.itemParse(Constants.PECHERAS_PATH)
}

pop = Population(30, items_information, Crossing.onePointCrossing, None, Elite.select)
pop.generateRandomPopulation()

for i in range(0, 10):
    (avgF, minF) = pop.getFitnessOfPopulation()
    print(str(i) +  " - Avg: " + str(avgF) + " Min: " + str(minF)) 
    pop.performSelection()



# with open('config.json') as config:
#     data = json.load(config)

# crossing = data['crossing']
# mutation = data['mutation']
# selector = data['selector']
# implementation = data["implementation"]
# stop = data["stop"]
# character = data["character"]
# pm = data["pm"]

