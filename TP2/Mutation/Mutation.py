import random 
from Utilities import Constants

class Mutation:

    @classmethod
    def geneMutation(pm,character, items_info):
        #muta solo un gen con prob pm
        muta = random.random()
        geneList = character.get_genes()
        if muta <= pm:
            geneIdx = random.randint(0, Constants.GENES_SIZE) #agarro el gen que muta
            geneList[geneIdx] = self.mutateGene(Constants.GENES_LIST[geneIdx],items_info)
        character.set_new_genes(geneList)
        return character

    @classmethod
    def limitedMultigene(pm,character,items_info):
        #se selecciona random M genes para mutar
        m = random.randrange(Constants.GENES_SIZE)
        geneList = character.get_genes() 
        selectedGenes = random.sample(geneList, m)
        for gene in selectedGenes:
            muta = random.random() #muta con prob pm
            if muta <= pm:
                geneList[gene] = self.mutateGene(Constants.GENES_LIST[gene],items_info) 
        character.set_new_genes(geneList)        
        return character
    

    @classmethod
    def uniformMultigene(pm,character,items_info):
        #todos los genes tienen prob pm de mutar
        geneList = character.get_genes()
        for gene in range(Constants.GENES_SIZE):
            muta = random.random()
            if muta <= pm:
                geneList[gene] = self.mutateGene(Constants.GENES_LIST[gene],items_info)
        character.set_new_genes(geneList)        
        return character        

    @classmethod
    def geneComplete(pm,character,items_info):
        #mutan todos con prob pm (o todos o ninguno)
        muta = random.random()
        geneList = character.get_genes()
        if muta <= pm:
            for gene in range(Constants.GENES_SIZE):
                geneList[gene] = self.mutateGene(Constants.GENES_LIST[gene],items_info) 
        character.set_new_genes(geneList)
        return character

    
    def mutateGene(self, name, items_info):
        if name == Constants.GEN_HEIGHT:
            return 1.3 + random.random()* 0.7 # h entre [1.3; 2]
        geneIdx = random.randrange(Constants.ITEMS_SIZE) #el nuevo idx es el de la posicion itemsInformation[name][geneIdx]
        return items_info[name][geneIdx]