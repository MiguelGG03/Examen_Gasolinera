import time
from Gasolinera import Surtidor,Gasolinera

class Coche():

    def __init__(self):
        self.repostado = False

    def repostar(self, surtidor:Surtidor):
        if surtidor.getEnUso() == False:
            self.repostado = True
            inicio=time.time()
            tiempo_a_esperar = surtidor.getTiempo()
            surtidor.setEnUso(True)
            print("Repostando...")
            while time.time()-inicio < tiempo_a_esperar:
                time.sleep(0.5)
            

    def getRepostado(self):
        return self.repostado
    

if __name__=='__main__':
    coches = []
    for i in range(10):
        coches.append(Coche())
    gas = Gasolinera()
    print(gas.cuantos_surtidores_str())