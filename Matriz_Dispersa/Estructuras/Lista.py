
from abc import ABC, abstractmethod

class Lista(ABC):
    def __init__(self):
        self.primero = None
        self.ultimo = None

    @abstractmethod
    def insertar(self):
        pass

    @abstractmethod
    def imprimir(self):
        pass