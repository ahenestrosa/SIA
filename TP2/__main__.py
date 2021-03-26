from Character import Character
from Utilities import Utilities
from Utilities import Constants
from Population import Population
from Selection import Elite
from Selection import Roulette
from Selection import Ranking
from Selection import Universal


botas = Utilities.itemParse(Constants.BOTAS_PATH)
armas = Utilities.itemParse(Constants.ARMAS_PATH)
pecheras = Utilities.itemParse(Constants.PECHERAS_PATH)
guantes = Utilities.itemParse(Constants.GUANTES_PATH)
cascos = Utilities.itemParse(Constants.CASCOS_PATH)

items_information = {
    Constants.BOTA: botas,
    Constants.ARMA: armas,
    Constants.CASCO: cascos,
    Constants.GUANTE: guantes,
    Constants.PECHERA: pecheras
}

pop = Population(30, items_information)
pop.generateRandomPopulation()

