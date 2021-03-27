from Character import Character
from Utilities import Utilities
from Utilities import Constants
from Population import Population
from Selection import Elite
from Selection import Roulette
from Selection import Ranking
from Selection import Universal
from crossing.Crossing import Crossing


items_information = {
    Constants.BOTA:    Utilities.itemParse(Constants.BOTAS_PATH),
    Constants.ARMA:    Utilities.itemParse(Constants.ARMAS_PATH),
    Constants.CASCO:   Utilities.itemParse(Constants.CASCOS_PATH),
    Constants.GUANTE:  Utilities.itemParse(Constants.GUANTES_PATH),
    Constants.PECHERA: Utilities.itemParse(Constants.PECHERAS_PATH)
}

pop = Population(5, items_information)
pop.generateRandomPopulation()

p1 = pop.characters[0]
p2 = pop.characters[1]

(c1, c2) = Crossing.unifromCrossing(p1, p2)

print(p1)
print(p2)
print(c1)
print(c2)

