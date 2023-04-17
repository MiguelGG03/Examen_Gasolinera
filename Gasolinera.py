import random

class Gasolinera():
    """
    Solo voy a hacer el programa para 4 surtidores
    N=4
    """
    # Constructor
    def __init__(self):
        self.surtidores=[]
        self.surtidor1,self.surtidor2,self.surtidor3,self.surtidor4=Surtidor(),Surtidor(),Surtidor(),Surtidor()
        self.surtidores.append(self.surtidor1)
        self.surtidores.append(self.surtidor2)
        self.surtidores.append(self.surtidor3)
        self.surtidores.append(self.surtidor4)
    
    # Getters
    def getSurtidores(self):
        return self.surtidores
    
    def cuantos_surtidores_str(self):
        return "Gasolinera con " + str(len(self.surtidores)) + " surtidores"
    
    def __str__(self):
        return f"Surtidor {self.surtidor1.getId()} - "
    
    

class Surtidor():
    # Constructor
    def __init__(self):
        self.id=random.randrange(300)
        self.en_uso=False
        self.tiempo=random.randrange(5,10) # En vez de ser de 5 a 10 minutos es de 5 a 10 segundos

    # Getters
    def getId(self)-> int:
        return self.id

    def getTiempo(self)-> int:
        return self.tiempo
    
    def getEnUso(self)-> bool:
        return self.en_uso
    
    # Setters
    def setTiempo(self, tiempo:int):
        self.tiempo=tiempo

    def setEnUso(self, en_uso:bool):
        self.en_uso=en_uso

    def print_uso(self):
        if self.en_uso:
            print("Surtidor en uso")
        else:
            print("Surtidor libre")
