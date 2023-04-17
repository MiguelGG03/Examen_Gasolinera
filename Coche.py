import time
from Gasolinera import Surtidor

class Coche():

    def __init__(self):
        self.repostado = False

    def repostar(self, surtidor:Surtidor):
        if surtidor.getEnUso() == False:
            tiempo_a_esperar = surtidor.getTiempo()
            surtidor.setEnUso(True)
            while time.time() < tiempo_a_esperar:
                print("Repostando...")
                time.sleep(1)
            self.repostado = True

    def getRepostado(self):
        return self.repostado
    
if __name__=="__main__":
    coche = Coche()
    surtidor = Surtidor()
    coche.repostar(surtidor)
    print(coche.getRepostado())