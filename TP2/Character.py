import math
from Utilities import Constants
from Utilities import Utilities

class Character:
    attack = 0
    defense = 0
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

    def calculate_stats(self):
        self._calculate_item_stats()


items = [{'type' : Constants.GUANTE, 'id' : 5}, {'type' : Constants.CASCO, 'id' : 5},{'type' : Constants.ARMA, 'id' : 5},{'type' : Constants.PECHERA, 'id' : 5}]
char = Character(Constants.GUERRERO, 1.7, items)
char.calculate_stats()

print(char)


