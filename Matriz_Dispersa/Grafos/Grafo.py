import os

from Matriz.Matriz import Matriz

class Grafo:
    def __init__(self):
        pass

    def generarMatriz(self, matriz):
        acumInfo = """digraph G{
node[shape=box, style=filled, color=deepskyblue3];
edge[color=black];
rankdir=UD;\n"""

        idCabeceraFila = ""
        cabeceraFila = ""

        idCabeceraCol = ""
        cabeceraCol = ""

        alineacionCol = "{rank=min; Matriz;"
        alineacionElementosFila = ""
        alineacionElementosColumna= ""

        cabeceraElementosFila = ""
        enlacesElementosFila = ""

        cabeceraElementosColumna = ""
        enlacesElementosColumna= ""

        # RECORRIDO DE FILAS
        eFila = matriz.encFila.primero
        if eFila != None:
            cabeceraFila += 'Matriz -> "{}";\n'.format(str(hash(eFila)))
            #RECORRER TODAS LAS FILAS DE LA MATRIZ

            while eFila != None:
                #elemntos fila
                alineacionElementosFila += '{{rank=same; {};'.format(str(hash(eFila)))
                infoFilas = self.recorrerFilasMatriz(eFila)
                alineacionElementosFila += infoFilas[0] + "}\n"
                cabeceraElementosFila += infoFilas[1] + "\n"
                enlacesElementosFila += infoFilas[2] + "\n"


                idCabeceraFila += '"{}"[label = "{}"];\n'.format(str(hash(eFila)),str(eFila.getValue()))
                if eFila.siguiente != None:
                    #filas
                    cabeceraFila += '"{}" -> "{}";\n'.format(str(hash(eFila)),str(hash(eFila.siguiente)))
                eFila = eFila.siguiente

            # idCabeceraFila += '"{}"[label = "{}"];\n'.format(str(hash(eFila)), str(eFila.getValue()))
            # # elemntos fila
            # alineacionElementosFila += '{{rank=same; {};'.format(str(hash(eFila)))
            # infoFilas = self.recorrerFilasMatriz(eFila)
            # alineacionElementosFila += infoFilas[0] + "}\n"
            # cabeceraElementosFila += infoFilas[1] + "\n"
            # enlacesElementosFila += infoFilas[2] + "\n"



        # RECORRIDO DE COLUMNAS
        eCol = matriz.encColumna.primero
        if eCol != None:
            cabeceraCol += 'Matriz -> "{}";\n'.format(str(hash(eCol)))
            while eCol != None:
                # elemntos Columna
                # alineacionElementosColumna += '{{rank=same; {};'.format(str(hash(eCol)))
                infoCols = self.recorrerColumnasMatriz(eCol)
                # alineacionElementosColumna += infoCols[0] + "}\n"
                # cabeceraElementosColumna += infoCols[1] + "\n"
                enlacesElementosColumna += infoCols[2] + "\n"

                #COLUMNAS
                alineacionCol += '"{}";'.format(str(hash(eCol)))
                idCabeceraCol += '"{}"[label="{}"];\n'.format(str(hash(eCol)),str(eCol.getValue()))
                if eCol.siguiente != None:
                    cabeceraCol += '"{}" -> "{}";\n'.format(str(hash(eCol)),str(hash(eCol.siguiente)))
                else:
                    alineacionCol += '}\n\n'
                eCol = eCol.siguiente

            # alineacionCol += '"{}";}};\n\n'.format(str(hash(eCol)))
            # idCabeceraCol += '"{}"[label="{}"];\n'.format(str(hash(eCol)), str(eCol.getValue()))
            # elemntos Columna
            # alineacionElementosColumna += '{{rank=same; {};'.format(str(hash(eCol)))
            # infoCols = self.recorrerColumnasMatriz(eCol)
            # alineacionElementosColumna += infoCols[0] + "}\n"
            # cabeceraElementosColumna += infoCols[1] + "\n"
            # enlacesElementosColumna += infoCols[2] + "\n"

        acumInfo += alineacionCol + alineacionElementosFila  + alineacionElementosColumna\
                    + idCabeceraCol + idCabeceraFila  + cabeceraElementosFila +\
                     cabeceraElementosColumna + cabeceraCol + \
                    cabeceraFila +  enlacesElementosFila + \
                    enlacesElementosColumna + "\n}\n"

        f = open('grafo.dot','w')
        try:
            f.write(acumInfo)
        finally:
            f.close()

        prog = "dot -Tpng  grafo.dot -o grafo.png"
        os.system(prog)

    def recorrerFilasMatriz(self,nodoFila):
        rank = ""
        enlaces = ""
        cabeceras = ""
        tmp = nodoFila.derecha
        enlaces += '"{}" -> "{}";\n'.format(str(hash(nodoFila)), str(hash(tmp)))
        while tmp != None:
            rank += '"{}";'.format(str(hash(tmp)))
            cabeceras += '"{}"[label = "{}"];\n'.format(str(hash(tmp)), str(tmp.getValue()))
            if tmp.derecha != None:
                enlaces += '"{}" -> "{}";\n'.format(str(hash(tmp)), str(hash(tmp.derecha)))
            tmp = tmp.derecha
        # cabeceras += '"{}"[label = "{}"];\n'.format(str(hash(tmp)), str(tmp.getValue()))
        return [rank,cabeceras,enlaces]

    def recorrerColumnasMatriz(self,nodoCol):
        rank = ""
        enlaces = ""
        cabeceras = ""
        tmp = nodoCol.abajo
        enlaces += '"{}" -> "{}";\n'.format(str(hash(nodoCol)), str(hash(tmp)))
        while tmp != None:
            rank += '"{}";'.format(str(hash(tmp)))
            cabeceras += '"{}"[label = "{}"];\n'.format(str(hash(tmp)), str(tmp.getValue()))
            if tmp.abajo != None:
                enlaces += '"{}" -> "{}";\n'.format(str(hash(tmp)), str(hash(tmp.abajo)))
            tmp = tmp.abajo
        # cabeceras += '"{}"[label = "{}"];\n'.format(str(hash(tmp)), str(tmp.getValue()))
        return [rank,cabeceras,enlaces]