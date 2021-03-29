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
    characterId = 0
    fitness = 0
    def __init__(self, pj_class, height, items, characterId):
        self.pj_clas = pj_class
        self.height = height
        self.items = items
        self.characterId = characterId
        self.calculate_stats()


    def _calculate_item_stats(self):
        for item in self.items.values():
            self._sum_item_stats(item)


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
        self.calculate_fitness()

    def calculate_fitness(self):
        if(self.pj_clas == Constants.GUERRERO):
            self.fitness = 0.6 * self.attack + 0.6 * self.defense
            return self.fitness
        elif(self.pj_clas == Constants.ARQUERO):
            self.fitness = 0.9 * self.attack + 0.1 * self.defense
            return self.fitness
        elif (self.pj_clas == Constants.DEFENSOR):
            self.fitness = 0.3 * self.attack + 0.8 * self.defense
            return self.fitness
        elif (self.pj_clas == Constants.INFILTRADO):
            self.fitness = 0.8 * self.attack + 0.3 * self.defense
            return self.fitness

    def get_genes(self):
        return [self.height, self.items[Constants.BOTA], self.items[Constants.ARMA], self.items[Constants.CASCO], self.items[Constants.GUANTE], self.items[Constants.PECHERA]]

    def set_new_genes(self, newGenes):
        self.height  = newGenes[0] 
        self.items[Constants.BOTA]  = newGenes[1] 
        self.items[Constants.ARMA]  = newGenes[2] 
        self.items[Constants.CASCO]  = newGenes[3] 
        self.items[Constants.GUANTE]  = newGenes[4] 
        self.items[Constants.PECHERA]  = newGenes[5]
        self.calculate_stats()


    def __lt__(self, other):
        return self.fitness < other.fitness

    def __str__(self):
         rep = "Character id: " + str(self.characterId) + "\n"
         rep += "   Height: " + str(self.height) + "\n"
         rep += "   Class: " + str(self.pj_clas) + "\n"
         rep += "   Attack: " + str(self.attack) + "\n"
         rep += "   Defense: " + str(self.defense) + "\n"
         rep += "   Fitness: " + str(self.fitness) +"\n"
         for k in self.items:
             rep += "       " + str(k) + ": " + str(self.items[k][Constants.ID]) + "\n" 
         return rep


    
