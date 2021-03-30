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
from Mutation.Mutation import Mutation

import json

with open('config.json') as config:
    data = json.load(config)

populationSize = data['populationSize']
crossing = data['crossing']
mutation = data['mutation']
selector = data['selector']
implementation = data["implementation"]
endingCondition = data["endingCondition"]
character = data["character"]
pm = data["pm"]
selectionChilds = data["selectionChilds"]
fillMethod = data["fillMethod"]


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
    extraSelectionArgument = "it"
elif selector == "TOURNAMENT_P":
    selectionMethod = TournamentP.select
    extraSelectionArgument = 0.7
elif selector == "TOURNAMENT_D":
    selectionMethod = TournamentD.select
    extraSelectionArgument = 5
elif selector == "ROULETTE":
    selectionMethod = Roulette.select
elif selector == "UNIVERSAL":
    selectionMethod = Universal.select

endingParameters = None
if endingCondition == "ACC_SOL":
    endingParameters = (data["endingFitnessLimit"],)
elif endingCondition == "CONTENT":
    endingParameters = (data["endingDeltaFitness"],)
elif endingCondition == "GEN_AMMOUNT":
    endingParameters = (data["endingGenerationsLimit"],)
elif endingCondition == "STRUCTURE":
    endingParameters = (data["endingStructureDh"], data["endingStructureDad"], data["endingStructureDf"], data["endingStructurePp"]) 
elif endingCondition == "TIME":
    endingParameters = (data["endingTimeLimit"],)
else:
    exit(1)


pop = Population(character,
                populationSize, 
                items_information, 
                Crossing.twoPointCrossing, 
                Mutation.uniformMultigene,
                pm,
                selectionMethod,
                selectionChilds,
                fillMethod,
                extraSelectionArgument)
                
pop.generateRandomPopulation()
pop.performLifeCycle(endingCondition, endingParameters)




