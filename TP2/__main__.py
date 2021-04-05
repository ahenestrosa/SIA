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
import time
import json

def getSelectionMethod(selector, t0_temp, tc_temp, k_temp, td_m, tp_treshold):
    selectionMethod = None
    extraSelectionArgument = None
    if selector == "ELITE":
        selectionMethod = Elite.select
    elif selector == "RANKING":
        selectionMethod = Ranking.select
    elif selector == "BOLTZMANN":
        selectionMethod = Boltzmann.select
        extraSelectionArgument = (t0_temp, tc_temp, k_temp)
    elif selector == "TOURNAMENT_P":
        selectionMethod = TournamentP.select
        extraSelectionArgument = (tp_treshold,)
    elif selector == "TOURNAMENT_D":
        selectionMethod = TournamentD.select
        extraSelectionArgument = (td_m,)
    elif selector == "ROULETTE":
        selectionMethod = Roulette.select
    elif selector == "UNIVERSAL":
        selectionMethod = Universal.select
    else:
        print("Invalid Selection Method.")
        exit(1)
    
    return (selectionMethod, extraSelectionArgument)

with open('config.json') as config:
    data = json.load(config)

populationSize = data['populationSize']
crossing = data['crossing']
mutation = data['mutation']
selector1 = data['selector1']
selector2 = data['selector2']
selector3 = data['selector3']
selector4 = data['selector4']
selectorA = data['selectorA']
selectorB = data['selectorB']
endingCondition = data["endingCondition"]
character = data["character"]
pm = data["pm"]
selectionChilds = data["selectionChilds"]
fillMethod = data["fillMethod"]

t0_temp = data["t0_temp"]
tc_temp = data["tc_temp"]
k_temp = data["k_temp"]
tp_treshold = data['tp_threshold']
td_m = data['td_m']



items_information = {
    Constants.BOTA:    Utilities.itemParse(Constants.BOTAS_PATH),
    Constants.ARMA:    Utilities.itemParse(Constants.ARMAS_PATH),
    Constants.CASCO:   Utilities.itemParse(Constants.CASCOS_PATH),
    Constants.GUANTE:  Utilities.itemParse(Constants.GUANTES_PATH),
    Constants.PECHERA: Utilities.itemParse(Constants.PECHERAS_PATH)
}

crossingMethod = None
if crossing == "ONE-POINT":
    crossingMethod = Crossing.onePointCrossing
elif crossing == "TWO-POINT":
    crossingMethod = Crossing.twoPointCrossing
elif crossing == "ANULAR":
    crossingMethod = Crossing.anularCrossing
elif crossing == "UNIFORM":
    crossingMethod = Crossing.unifromCrossing
else:
    print("Invalid Crossing Method.")
    exit(1)

mutationMethod = None
if mutation == "GENE":
    mutationMethod = Mutation.geneMutation
elif mutation == "LIMITED-MULTIGENE":
    mutationMethod = Mutation.limitedMultigene
elif mutation == "UNIFORM":
    mutationMethod = Mutation.uniformMultigene
elif mutation == "GENE-COMPLETE":
    mutationMethod = Mutation.geneComplete
else:
    print("Invalid Mutation Method.")
    exit(1)


selectionMethod1 = getSelectionMethod(selector1, t0_temp, tc_temp, k_temp, td_m, tp_treshold)
selectionMethod2 = getSelectionMethod(selector2, t0_temp, tc_temp, k_temp, td_m, tp_treshold)
selectionMethod3 = getSelectionMethod(selector3, t0_temp, tc_temp, k_temp, td_m, tp_treshold)
selectionMethod4 = getSelectionMethod(selector4, t0_temp, tc_temp, k_temp, td_m, tp_treshold)

endingParameters = None
if endingCondition == "ACC_SOL":
    endingParameters = (data["endingFitnessLimit"],)
elif endingCondition == "CONTENT":
    endingParameters = (data["endingGenerationsCompared"],data["endingDeltaFitness"],)
elif endingCondition == "GEN_AMMOUNT":
    endingParameters = (data["endingGenerationsLimit"],)
elif endingCondition == "STRUCTURE":
    endingParameters = (data["endingGenerationsCompared"], data["endingStructureDh"], data["endingStructureDad"], data["endingStructureDf"], data["endingStructurePp"])
elif endingCondition == "TIME":
    endingParameters = (data["endingTimeLimit"],)
else:
    print("Invalid Ending Method.")
    exit(1)


start_time = time.time()

pop = Population(character,
                populationSize, 
                items_information, 
                crossingMethod, 
                mutationMethod,
                pm,
                selectionMethod1,
                selectionMethod2,
                selectionMethod3,
                selectionMethod4,
                selectorA,
                selectorB,
                selectionChilds,
                fillMethod,
                )
                
pop.generateRandomPopulation()
pop.performLifeCycle(endingCondition, endingParameters)

end_time = time.time()
time = round(end_time-start_time, 4)
print("Time: " + str(time))


exit(0)





