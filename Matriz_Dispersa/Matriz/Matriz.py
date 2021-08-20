from Objetos.Dia import Dia
from Objetos.Hora import Hora
from Matriz.Encabezado import Encabezado
from Matriz.ListaComida import  ListaComida

class Matriz:
    def __init__(self):
        self.encFila = Encabezado()
        self.encColumna = Encabezado()

    def inertar(self,_hora,_dia,comida):
        #insertando en filas
        hora = Hora(_hora)
        resFila = self.encFila.insertar(hora)

        #insertando en columnas
        dia = Dia(_dia)
        resCol = self.encColumna.insertar(dia)



        #Encabezados nuevos
        if resFila.derecha == None and resCol.abajo == None:
            nuevolc = self.nuevaListaComida(_hora,_dia,comida)
            #ASOCIANDO CABECERAS
            resFila.derecha = nuevolc
            resCol.abajo = nuevolc
        elif resFila.derecha != None and resCol.abajo == None: #FILA EXISTE  COLUMNA NO
            # enlazamos la nueva cabecera
            nuevolc = self.nuevaListaComida(_hora,_dia,comida)
            resCol.abajo = nuevolc
            # trabajo con el valor de las columnas
            #insercion al inicio
            if nuevolc.columna < resFila.derecha.columna:
                nuevolc.derecha = resFila.derecha
                resFila.derecha.izquierda = nuevolc
                resFila.derecha = nuevolc
            else:
                tmp = resFila.derecha
                flagInsercion = False
                while tmp.derecha != None:
                    if nuevolc.columna > tmp.columna and nuevolc.columna < tmp.derecha.columna: #INERCION AL MEDIO
                        nuevolc.derecha = tmp.derecha
                        tmp.derecha.izquierda = nuevolc
                        tmp.derecha = nuevolc
                        nuevolc.izquierda = tmp
                        flagInsercion = True
                    tmp = tmp.derecha

                if not flagInsercion:  #INSERCION AL FINAL
                    tmp.derecha = nuevolc
                    nuevolc.izquierda = tmp

        elif resFila.derecha == None and resCol.abajo != None: #COLUMNA EXISTE ; FILA NO
            # enlazamos la nueva cabecera
            nuevolc = self.nuevaListaComida(_hora, _dia, comida)
            resFila.derecha = nuevolc
            # trabajo con el valor de las columnas
            # insercion al inicio
            if nuevolc.fila < resCol.abajo.fila:
                nuevolc.abajo = resCol.abajo
                resCol.abajo.arriba = nuevolc
                resCol.abajo = nuevolc
            else:
                tmp = resCol.abajo
                flagInsercion = False
                while tmp.abajo != None:
                    if nuevolc.fila > tmp.fila and nuevolc.fila < tmp.abajo.fila:  # INERCION AL MEDIO
                        nuevolc.abajo = tmp.abajo
                        tmp.abajo.arriba = nuevolc
                        tmp.abajo = nuevolc
                        nuevolc.arriba = tmp
                        flagInsercion = True
                    tmp = tmp.abajo

                if not flagInsercion:  # INSERCION AL FINAL
                    tmp.abajo = nuevolc
                    nuevolc.arriba = tmp
        else: # aca si existen las cabeceras
            nuevolc = self.nuevaListaComida(_hora, _dia, comida)
            flagInsFila = False
            flagInsCol = False

            #VALIDACIONES DEL INICIO
            #filas
            if nuevolc.columna < resFila.derecha.columna:
                nuevolc.derecha = resFila.derecha
                resFila.derecha.izquierda = nuevolc
                resFila.derecha = nuevolc
                flagInsFila = True
            if nuevolc.fila < resCol.abajo.fila:
                nuevolc.abajo = resCol.abajo
                resCol.abajo.arriba = nuevolc
                resCol.abajo = nuevolc
                flagInsCol = True

            if not flagInsFila and flagInsCol:
                #encontrar el nulo de la fila
                tmpFila = resFila.derecha
                while tmpFila.derecha != None:
                    tmpFila = tmpFila.derecha

                tmpFila.derecha = nuevolc
                nuevolc.izquierda = tmpFila

            elif not flagInsCol and flagInsFila:
                tmpCol = resCol.abajo
                while tmpCol.abajo != None:
                    tmpCol = tmpCol.abajo
                tmpCol.abajo = nuevolc
                nuevolc.arriba = tmpCol
            # continua complentando el codigo  con las flags para completar los algoritmos de insercion

            # elif not flagInsCol and not flagInsFila:
                #......
                

    def nuevaListaComida(self,_hora,_dia,comida):
        listaComida = ListaComida();
        listaComida.insertar(_hora, _dia, comida)
        return listaComida
