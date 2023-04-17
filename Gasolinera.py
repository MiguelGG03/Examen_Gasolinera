import random

class Gasolinera():
    # Constructor
    def __init__(self, surtidores):
        self.surtidores=surtidores
    
    # Getters
    def getSurtidores(self):
        return self.surtidores
    
    def SurtidorLibre(self):
        for surtidor in self.surtidores:
            if surtidor.getTiempo() == 0:
                return surtidor
        return None
    
    

class Surtidor():
    # Constructor
    def __init__(self):
        self.en_uso=False
        self.tiempo=random.randrange(5,10)

    # Getters
    def getTiempo(self):
        return self.tiempo
    
    def getEnUso(self)-> bool:
        return self.en_uso
    
    # Setters
    def setTiempo(self, tiempo):
        self.tiempo=tiempo

    def setEnUso(self, en_uso:bool):
        self.en_uso=en_uso

