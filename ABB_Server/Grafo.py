

class Grafo:
    def __init__(self):
        pass

    def graficarArbol(self, raiz):
        acumuladores = ["digraph G{\nnode [shape=circle];\n", ""]

        if raiz != None:
            self.recorrerArbol(raiz,acumuladores)

        acumuladores[0] += acumuladores[1] + "\n}"
        print(acumuladores[0])

    def recorrerArbol(self, raiz,acum):

        if raiz:
            acum[1] += '"{}"[label="{}"];\n'.format(str(hash(raiz)),str(raiz.id))

            if raiz.izq.raiz != None:
                acum[1] += '"{}" -> "{}";\n'.format(str(hash(raiz)),str(hash(raiz.izq.raiz)))
            if raiz.der.raiz != None:
                acum[1] += '"{}" -> "{}";\n'.format(str(hash(raiz)), str(hash(raiz.der.raiz)))

            self.recorrerArbol(raiz.izq.raiz, acum)
            self.recorrerArbol(raiz.der.raiz, acum)
