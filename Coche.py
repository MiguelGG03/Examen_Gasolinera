import time
from Gasolinera import Surtidor,Gasolinera
import random
from multiprocessing import Pool,Queue,Process

class Coche():

    def __init__(self):
        self.id=random.randrange(1000,9999)
        self.repostado = False
        self.puede_repostar = False
        self.surtidor = None
        self.tiempo=random.randrange(5,10) # En vez de ser de 5 a 10 minutos es de 5 a 10 segundos

    def getId(self):
        return self.id

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
                print(f"Surtidor {str(surtidor.getId())} asignado al coche {str(self.getId())}")
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

def crear_coches(queue):
    for _ in range(100):
        queue.put(Coche())
    return queue   

if __name__=='__main__':
    q = Queue()
    gas = Gasolinera()
    crear_coches(q)

    while q.qsize()!=0:

        print(q.get())
        with Pool(4) as p:
            if gas.check_surtidores():
                for i in range(q.qsize()):
                    surtidor = q.get(i).ConsigueSurtidor(gas.getSurtidores())
                    print(gas.str())
                    print()
                    if surtidor != None:
                        p.apply_async(q.get(i).repostar, args=(surtidor,))
                        #q.task_done(q.get(i))