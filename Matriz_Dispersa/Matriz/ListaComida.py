from Estructuras.Lista import Lista
from Estructuras.Nodo import  Nodo

class ListaComida(Lista, Nodo):
    def __init__(self):
        Nodo.__init__(self)
        Lista.__init__(Nodo)
        self.fila = 0
        self.columna = 0


    def insertar(self,fila,columna, comida):
        self.fila = fila
        self.columna = columna
        if self.primero == None:
            self.primero = comida
            self.ultimo = comida
        else: #insertando al ultimo
            self.ultimo.siguiente = comida
            comida.anterior = self.ultimo
            self.ultimo = comida

    def imprimir(self):
        tmp = self.primero
        while tmp != None:
            print(tmp.getValue())
            tmp = tmp.siguiente

    def getValue(self):
        tmp = self.primero
        acum = ""
        while tmp != None:
            acum += tmp.getValue() +" "
            tmp = tmp.siguiente
        return acum

