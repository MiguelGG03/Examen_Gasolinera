import time
from Gasolinera import Surtidor,Gasolinera
import random
from multiprocessing import Pool

class Coche():

    def __init__(self):
        self.repostado = False
        self.puede_repostar = False
        self.surtidor = None
        self.tiempo=random.randrange(5,10) # En vez de ser de 5 a 10 minutos es de 5 a 10 segundos

    def getRepostado(self):
        return self.repostado
    
    def getTiempo(self):
        return self.tiempo
    
    def ConsigueSurtidor(self,surtidores):
        for surtidor in surtidores:
            if surtidor.getEnUso() == False:
                surtidor.setEnUso(True)
                self.puede_repostar = True
                self.surtidor = surtidor
                print(f"Surtidor {str(surtidor.getId())} asignado al coche {str(self)}")
                return surtidor
        return None
    
    def repostar(self, surtidor:Surtidor):
            self.repostado = True
            inicio=time.time()
            tiempo_a_esperar = self.getTiempo()
            surtidor.setEnUso(True)
            print("Repostando...")
            while time.time()-inicio < tiempo_a_esperar:
                time.sleep(0.5)
            surtidor.setEnUso(False)

    

if __name__=='__main__':
    coches = []
    for i in range(100):
        coches.append(Coche())
    gas = Gasolinera()
    while len(coches)!=0:
        with Pool(4) as p:
            if gas.check_surtidores():
                for coche in coches:
                    surtidor = coche.ConsigueSurtidor(gas.getSurtidores())
                    print(gas.str())
                    if surtidor != None:
                        p.apply_async(coche.repostar, args=(surtidor,))
                        coches.remove(coche)