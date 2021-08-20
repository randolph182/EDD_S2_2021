from abc import ABC, abstractmethod

class Nodo(ABC):
    def __init__(self):
        self.izquierda  = None
        self.derecha = None
        self.arriba = None
        self.abajo = None


        self.siguiente = None
        self.anterior = None

    @abstractmethod
    def imprimir(self):
        pass

    @abstractmethod
    def getValue(self):
        pass