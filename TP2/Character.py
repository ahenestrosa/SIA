import math
from Utilities import Constants
from Utilities import Utilities

class Character:
    attack = 0
    defense = 0
    force = 0
    agility = 0
    expertise = 0
    resistance = 0
    health = 0
    items_stats = {Constants.FUERZA: 0, Constants.VIDA: 0, Constants.RESISTENCIA: 0, Constants.PERICIA: 0, Constants.AGILIDAD: 0}
    def __init__(self, pj_class, height, items):
        self.pj_clas = pj_class
        self.height = height
        self.items = items


    def _calculate_item_stats(self):
        for item in self.items:
            found_item = {}
            id = item['id']
            if item['type'] == Constants.GUANTE:
                found_item = Utilities.findItem(Constants.GUANTES_PATH, id)
            elif item['type'] == Constants.CASCO:
                found_item = Utilities.findItem(Constants.CASCOS_PATH, id)
            elif item['type'] == Constants.ARMA:
                found_item = Utilities.findItem(Constants.ARMAS_PATH, id)
            elif item['type'] == Constants.PECHERA:
                found_item = Utilities.findItem(Constants.PECHERAS_PATH, id)
            elif item['type'] == Constants.BOTA:
                found_item = Utilities.findItem(Constants.BOTAS_PATH, id)
            self._sum_item_stats(found_item)


    def _sum_item_stats(self, f_item):
        self.items_stats = {Constants.FUERZA: self.items_stats[Constants.FUERZA] + f_item[Constants.FUERZA],
                            Constants.AGILIDAD:  self.items_stats[Constants.AGILIDAD] + f_item[Constants.AGILIDAD],
                            Constants.PERICIA:  self.items_stats[Constants.PERICIA] + f_item[Constants.PERICIA],
                            Constants.RESISTENCIA:  self.items_stats[Constants.RESISTENCIA] + f_item[Constants.RESISTENCIA],
                            Constants.VIDA:  self.items_stats[Constants.VIDA] + f_item[Constants.VIDA]}

    def _calculate_force(self):
        self.force += 100 * math.tanh(0.01 * self.items_stats[Constants.FUERZA])

    def _calculate_agility(self):
        self.agility += math.tanh(0.01 * self.items_stats[Constants.AGILIDAD])

    def _calculate_expertise(self):
        self.expertise += 0.6 * math.tanh(0.01 * self.items_stats[Constants.PERICIA])

    def _calculate_resistance(self):
        self.resistance += math.tanh(0.01 * self.items_stats[Constants.RESISTENCIA])

    def _calculate_health(self):
        self.health += 100 * math.tanh(0.01 * self.items_stats[Constants.VIDA])

    def _calculate_at_def(self):
        ATM =  0.7 - math.pow(3*self.height - 5, 4) + math.pow(3 * self.height - 5, 2) + self.height/4
        DEM = 1.9 + math.pow(2.5 * self.height - 4.16, 4) - math.pow(2.5 * self.height - 4.16, 2) - 3*self.height/10
        self.attack = (self.agility + self.expertise) * self.force * ATM
        self.defense = (self.resistance + self.expertise) * self.health * DEM


    def calculate_stats(self):
        self._calculate_item_stats()
        self._calculate_force()
        self._calculate_health()
        self._calculate_resistance()
        self._calculate_agility()
        self._calculate_expertise()
        self._calculate_at_def()



items = [{'type' : Constants.GUANTE, 'id' : 5}, {'type' : Constants.CASCO, 'id' : 5},{'type' : Constants.ARMA, 'id' : 5},{'type' : Constants.PECHERA, 'id' : 5}]
char = Character(Constants.GUERRERO, 1.7, items)
char.calculate_stats()

print(char)
