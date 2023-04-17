import random

class Gasolinera():
    """
    Solo voy a hacer el programa para 4 surtidores
    N=4
    """
    # Constructor
    def __init__(self):
        self.surtidores=[]
    
    # Getters
    def getSurtidores(self):
        return self.surtidores
    
    def __str__(self):
        return "Gasolinera con " + str(len(self.surtidores)) + " surtidores"
    
    

class Surtidor():
    # Constructor
    def __init__(self):
        self.id=round(random.random(300),0)
        self.en_uso=False
        self.tiempo=random.randrange(5,10) # En vez de ser de 5 a 10 minutos es de 5 a 10 segundos

    # Getters
    def getTiempo(self)-> int:
        return self.tiempo
    
    def getEnUso(self)-> bool:
        return self.en_uso
    
    # Setters
    def setTiempo(self, tiempo:int):
        self.tiempo=tiempo

    def setEnUso(self, en_uso:bool):
        self.en_uso=en_uso
