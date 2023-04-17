import time
from Gasolinera import Surtidor

class Coche():

    def repostar(self, surtidor:Surtidor):
        tiempo_a_esperar = surtidor.getTiempo()
        while time.time() < tiempo_a_esperar:
            print("Repostando...")
            time.sleep(1)