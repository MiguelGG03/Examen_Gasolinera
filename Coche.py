import time
from Gasolinera import Surtidor,Gasolinera
from multiprocessing import Pool

class Coche():

    def __init__(self):
        self.repostado = False
        self.puede_repostar = False
        self.surtidor = None

    def getRepostado(self):
        return self.repostado
    
    def ConsigueSurtidor(self,surtidores):
        for surtidor in surtidores:
            if surtidor.getEnUso() == False:
                surtidor.setEnUso(True)
                self.puede_repostar = True
                self.surtidor = surtidor
                return surtidor
        return None
    
    def repostar(self, surtidor:Surtidor):
            self.repostado = True
            inicio=time.time()
            tiempo_a_esperar = surtidor.getTiempo()
            surtidor.setEnUso(True)
            print("Repostando...")
            while time.time()-inicio < tiempo_a_esperar:
                time.sleep(0.5)

    

if __name__=='__main__':
    coches = []
    for i in range(10):
        coches.append(Coche())
    gas = Gasolinera()
    print(gas.str())
    p = Pool(5)
    p.map(Coche.repostar, coches)