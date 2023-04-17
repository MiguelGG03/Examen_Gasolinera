import time
from Gasolinera import Surtidor

class Coche():

    def __init__(self):
        self.repostado = False

    def repostar(self, surtidor:Surtidor):
        tiempo_a_esperar = surtidor.getTiempo()
        while time.time() < tiempo_a_esperar:
            print("Repostando...")
            time.sleep(1)
        self.repostado = True

    def getRepostado(self):
        return self.repostado