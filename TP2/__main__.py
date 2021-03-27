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

with open('config.json') as config:
    data = json.load(config)

crossing = data['crossing']
mutation = data['mutation']
selector = data['selector']
implementation = data["implementation"]
stop = data["stop"]
character = data["character"]
pm = data["pm"]


items_information = {
    Constants.BOTA:    Utilities.itemParse(Constants.BOTAS_PATH),
    Constants.ARMA:    Utilities.itemParse(Constants.ARMAS_PATH),
    Constants.CASCO:   Utilities.itemParse(Constants.CASCOS_PATH),
    Constants.GUANTE:  Utilities.itemParse(Constants.GUANTES_PATH),
    Constants.PECHERA: Utilities.itemParse(Constants.PECHERAS_PATH)
}

selectionMethod = None
extraSelectionArgument = None
if selector == "ELITE":
    selectionMethod = Elite.select
elif selector == "RANKING":
    selectionMethod = Ranking.select
elif selector == "BOLTZMANN":
    selectionMethod = Boltzmann.select
    extraSelectionArgument = 10
elif selector == "TOURNAMENT_P":
    selectionMethod = TournamentD.select
elif selector == "TOURNAMENT_D":
    selectionMethod = TournamentD.select
elif selector == "ROULETTE":
    selectionMethod = Roulette.select
elif selector == "UNIVERSAL":
    selectionMethod = Universal.select

pop = Population(30, items_information, Crossing.onePointCrossing, None, selectionMethod, extraSelectionArgument)
pop.generateRandomPopulation()

for i in range(0, 10):
    (avgF, minF) = pop.getFitnessOfPopulation()
    print(str(i) +  " - Avg: " + str(avgF) + " Min: " + str(minF)) 
    pop.performSelection()





