from Estructuras.Lista import Lista

class Encabezado(Lista):
    def __init__(self):
        Lista.__init__(self)



    def insertar(self, nuevo):
        if self.primero == None: # inserta al principio y devuelve el primero
            self.primero = nuevo
            self.ultimo = nuevo
            return self.primero

        elif  nuevo.getValue() < self.primero.getValue(): #insercion al inicio y lo retorna
            self.primero.anterior = nuevo
            nuevo.siguiente = self.primero
            self.primero = nuevo
            return self.primero

        elif nuevo.getValue() == self.primero.getValue(): #nuevo es igual a primero, retorna primero
            return self.primero

        elif nuevo.getValue() > self.ultimo.getValue(): # insercion al ultimo, returna ultimo
            self.ultimo.siguiente = nuevo
            nuevo.anterior = self.ultimo
            self.ultimo = nuevo
            return self.ultimo

        else: # INSERCION AL MEDIO
            tmp = self.primero
            while tmp.siguiente != None:
                if nuevo.getValue() > tmp.getValue() and nuevo.getValue() < tmp.siguiente.getValue():
                    tmp.siguiente.anterior = nuevo
                    nuevo.siguiente = tmp.siguiente
                    tmp.siguiente = nuevo
                    nuevo.anterior = tmp
                    return nuevo

                elif nuevo.getValue() == tmp.getValue(): #devuleve el valor que es igual
                    return tmp
                tmp = tmp.siguiente

            if nuevo.getValue() == tmp.getValue():  # devuleve el valor que es igual
                return tmp

    def imprimir(self):
        tmp = self.primero
        while tmp != None:
            print(tmp.getValue())
            tmp = tmp.siguiente