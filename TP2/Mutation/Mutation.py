import random 
from Utilities import Constants

class Mutation:

    def __init__(self, pm): #TODO: Agregarle el resto de los params
        self.pm = pm


    @staticmethod
    def genMutation(children):
        #muta solo un gen con prob pm
        muta = random.random()
        if muta <= pm:

            for child in children:

        return children            

    @staticmethod
    def limitedMultigen(children):
        #se selecciona random M genes para mutar
        for child in children:
            for selectedKey in selectedKeys:
                muta = rd.random()
                if muta <= pm:

        return children
    

    @staticmethod
    def uniformMultigen(children):
        #todos los genes tienen prob pm de mutar
        for child in children:
            for gene in range(Constants.GENES_LIST):
                muta = random.random()
                if muta <= pm:
                    
        return children        

    @staticmethod
    def genComplete(children):
        for child in children:
            muta = rd.random()
            if muta <= pm:
                for key in range(Constants.GENES_LIST):

        return children        
