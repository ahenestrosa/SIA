import random 
from Utilities import Constants

class Mutation:

    @classmethod
    def geneMutation(pm,character, allItems):
        #muta solo un gen con prob pm
        muta = random.random()
        if muta <= pm:
            geneIdx = random.randint(0, Constants.GENES_SIZE) #agarro el gen que muta
            character.items[geneIdx] = self.mutateGene(Constants.GENES_LIST[geneIdx],allItems)
        return character

    @classmethod
    def limitedMultigene(pm,character,allItems):
        #se selecciona random M genes para mutar
        m = random.randrange(Constants.GENES_SIZE)
        selectedGenes = random.sample(character.items, m) 
        for gene in selectedGenes:
            muta = random.random() #muta con prob pm
            if muta <= pm:
                character.items[gene] = self.mutateGene(Constants.GENES_LIST[gene],allItems) #TODO: check
        return character
    

    @classmethod
    def uniformMultigene(pm,character,allItems):
        #todos los genes tienen prob pm de mutar
        for gene in range(Constants.GENES_SIZE):
            muta = random.random()
            if muta <= pm:
                character.items[gene] = self.mutateGene(Constants.GENES_LIST[gene],allItems) #TODO: check
        return character        

    @classmethod
    def geneComplete(pm,character,allItems):
        #mutan todos con prob pm (o todos o ninguno)
        muta = random.random()
        if muta <= pm:
            for gene in range(Constants.GENES_SIZE):
                character.items[gene] = self.mutateGene(Constants.GENES_LIST[gene],allItems) #TODO: check
        return character

    
    def mutateGene(self, name, allGenes):
        if name == Constants.GEN_HEIGHT:
            return 1.3 + random.random()* 0.7 # h entre [1.3; 2]
        geneIdx = random.randrange(Constants.ITEMS_SIZE)
        #el nuevo idx es el de la posicion itemsInformation[name][geneIdx]
        # no se como enviarme itemsinfo
        return None