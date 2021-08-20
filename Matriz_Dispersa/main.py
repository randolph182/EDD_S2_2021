from Matriz.Matriz import Matriz
from  Matriz.Encabezado import Encabezado
from Objetos.Comida import Comida
from Grafos.Grafo import Grafo
def print_hi():
    platillo = Comida("spagetti","fideos")
    menu = Matriz()
    menu.inertar(1,1,platillo)
    menu.inertar(2, 1, platillo)
    menu.inertar(3, 2, platillo)
    menu.inertar(3, 1, platillo)
    menu.inertar(4, 2, platillo)
    menu.inertar(5, 1, platillo)
    menu.inertar(6, 2, platillo)
    menu.inertar(8, 1, platillo)
    menu.inertar(5, 6, platillo)
    g = Grafo()
    g.generarMatriz(menu)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
