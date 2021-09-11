
class Pagina:
    def __init__(self, orden):
        self.cuenta = 0;
        self.m = orden
        self.claves = [0 for x in range(orden)]
        self.ramas = [Pagina for x in range(orden)]

        #INICIALIZAMOS LAS PAGINAS
        for i in range(orden):
            self.ramas[i] = None

    def pagina_llena(self):
        return self.cuenta == self.m - 1

    def pagina_semi_llena(self):
        return self.cuenta < self.m / 2