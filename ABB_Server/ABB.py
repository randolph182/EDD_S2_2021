from Nodo import Node

class ABB:
    def __init__(self):
        self.raiz = None

    def insertar(self,_id,_nombre):
        nuevo = Node(_id,_nombre)
        if self.raiz == None:
            self.raiz = nuevo
            self.raiz.izq = ABB()
            self.raiz.der = ABB()
        elif _id > self.raiz.id:
            self.raiz.der.insertar(_id,_nombre)
        elif _id < self.raiz.id:
            self.raiz.izq.insertar(_id,_nombre)
        else: #YA EXISTE
            print("el valor ya existe")

    def enOrden(self):
        arr = []
        self.enOrden2(self.raiz,arr)
        return arr

    def enOrden2(self, raizActual,arr):
        if raizActual:
            self.enOrden2(raizActual.izq.raiz , arr )
            # print(raizActual.id)
            arr.append(
                {
                    "id":raizActual.id,
                    "nombre":raizActual.nombre
                }
            )
            self.enOrden2(raizActual.der.raiz , arr )