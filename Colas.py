class Cola():

    def __init__(self):
        self.items = []

    def estaVacia(self):
        return self.items == []

    def agregar(self, item):
        self.items.insert(0,item)

    def avanzar(self):
        return self.items.pop(0)

    def tamano(self):
        return len(self.items)

class ColaSurtidor(Cola):

    