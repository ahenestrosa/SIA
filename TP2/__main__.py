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
import itertools

def getCrossingMethod(crossing):
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
    
    return crossingMethod

def getMutationMethod(mutation):
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

    return mutationMethod

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

crossingMethod = getCrossingMethod(crossing)
mutationMethod = getMutationMethod(mutation)

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


########## Para ejecucion normal
start_time = time.time()
pop.performLifeCycle(endingCondition, endingParameters)
end_time = time.time()
time = round(end_time-start_time, 4)
print("Time: " + str(time))


########################## Para test masivo ##############################

#Config deberia estar en:
# "populationSize": 400,
#     "crossing": "UNIFORM",
#     "mutation": "UNIFORM",
#     "selector1": "BOLTZMANN",
#     "selector2": "TOURNAMENT_D",
#     "selector3": "TOURNAMENT_P",
#     "selector4": "BOLTZMANN",
#     "selectorA": 0.5,
#     "selectorB": 0.5,
#     "endingCondition": "GEN_AMMOUNT",
#     "character": "GUERRERO",
#     "pm": 0.5,
#     "selectionChilds": 200,
#     "fillMethod": "FILL_ALL",


#     "t0_temp" : 3,
#     "tc_temp" : 1.0,
#     "k_temp" : 0.1,
#     "tp_threshold": 0.75,
#     "td_m": 5,

#     "endingGenerationsCompared": 5,  
#     "endingFitnessLimit": 20    ,
#     "endingDeltaFitness": 1,
#     "endingGenerationsLimit": 100,
#     "endingStructureDh": 1,
#     "endingStructureDad": 1,
#     "endingStructureDf": 1,
#     "endingStructurePp": 1,
#     "endingTimeLimit": 10.0
# }



# CROSSING_LIST = ["ONE-POINT", "TWO-POINT", "ANULAR", "UNIFORM"]
# MUTATION_LIST = ["GENE", "LIMITED-MULTIGENE", "UNIFORM", "GENE-COMPLETE"]
# SELECTION_LIST= ["ELITE", "RANKING", "BOLTZMANN", "ROULETTE", "TOURNAMENT_D", "TOURNAMENT_P", "UNIVERSAL"]
# f = open("results.txt", "a")



# cases = 1

# selectionCombinations = []
# for elem in itertools.combinations(SELECTION_LIST, 2):
#     selectionCombinations.append(elem)
# for elem in SELECTION_LIST:
#     selectionCombinations.append((elem, elem))

# for cross in CROSSING_LIST:
#     for mut in MUTATION_LIST:
#         for selTuple in selectionCombinations:

#                 pop.crossing = getCrossingMethod(cross)
#                 pop.mutation = getMutationMethod(mut)
#                 pop.selectionMethod1 = getSelectionMethod(selTuple[0], t0_temp, tc_temp, k_temp, td_m, tp_treshold)
#                 pop.selectionMethod2 = getSelectionMethod(selTuple[1], t0_temp, tc_temp, k_temp, td_m, tp_treshold)
#                 pop.selectionMethod3 = getSelectionMethod(selTuple[0], t0_temp, tc_temp, k_temp, td_m, tp_treshold)
#                 pop.selectionMethod4 = getSelectionMethod(selTuple[1], t0_temp, tc_temp, k_temp, td_m, tp_treshold)

#                 (avgF, minF, maxF) = pop.performLifeCycleSummarized(endingCondition, endingParameters)

#                 f.write(cross + " " + mut + " " + selTuple[0] + " " + selTuple[1] + " " + str(avgF) + " "+ str(maxF) +" "+ str(minF) +"\n")

#                 print(str(cases)+ " covered")
#                 cases += 1


# f.close()


# CROSSING_LIST = ["ONE-POINT", "TWO-POINT", "ANULAR", "UNIFORM"]
# MUTATION_LIST = ["GENE", "LIMITED-MULTIGENE", "UNIFORM", "GENE-COMPLETE"]
# SELECTION_LIST_SUB_ELITE = ["RANKING", "BOLTZMANN", "ROULETTE", "TOURNAMENT_D", "TOURNAMENT_P", "UNIVERSAL"]
# ELITE_PROPORTION = [0.2, 0.8]
# MUTATION_PROB = [0.25, 0.75]

# f = open("results.txt", "a")

# cases = 1

# for cross in CROSSING_LIST:
#     for mut in MUTATION_LIST:
#         for sel in SELECTION_LIST_SUB_ELITE:
#             for proportion in ELITE_PROPORTION:
#                 for prob in MUTATION_PROB:

#                     pop.crossing = getCrossingMethod(cross)
#                     pop.mutation = getMutationMethod(mut)
#                     pop.selectionMethod1 = getSelectionMethod("ELITE", t0_temp, tc_temp, k_temp, td_m, tp_treshold)
#                     pop.selectionMethod2 = getSelectionMethod(sel, t0_temp, tc_temp, k_temp, td_m, tp_treshold)
#                     pop.selectionMethod3 = getSelectionMethod("ELITE", t0_temp, tc_temp, k_temp, td_m, tp_treshold)
#                     pop.selectionMethod4 = getSelectionMethod(sel, t0_temp, tc_temp, k_temp, td_m, tp_treshold)
#                     pop.selectorA = proportion
#                     pop.selectorB = proportion
#                     pop.mutationProb = prob

#                     (avgF, minF, maxF) = pop.performLifeCycleSummarized(endingCondition, endingParameters)

#                     f.write(cross + " " + mut + " " + sel + " " + str(proportion) + " " + str(avgF) + " "+ str(maxF) +" "+ str(minF) + " " + str(prob) +"\n")

#                     print(str(cases)+ " covered")
#                     cases += 1


# f.close()



exit(0)





