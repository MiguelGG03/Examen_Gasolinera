import random

class Gasolinera():
    # Constructor
    def __init__(self, surtidores):
        self.surtidores=surtidores
    
    # Getters
    def getSurtidores(self):
        return self.surtidores
    
    

class Surtidor():
    # Constructor
    def __init__(self):
        self.tiempo=random.randrange(5,10)

    # Getters
    def getTiempo(self):
        return self.tiempo

