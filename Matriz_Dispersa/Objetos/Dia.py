from Estructuras.Nodo import Nodo

class Dia(Nodo):
    def __init__(self,num):
        Nodo.__init__(self)
        self.numero = num

    def imprimir(self):
        return self.numero

    def getValue(self):
        return self.numero

