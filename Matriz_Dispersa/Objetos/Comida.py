from Estructuras.Nodo import Nodo

class Comida(Nodo):
    def __init__(self,_nombre,_ingrediente):
        Nodo.__init__(self)
        self.nombre = _nombre
        self.ingrediente = _ingrediente

    def imprimir(self):
        pass

    def getValue(self):
        return self.nombre
