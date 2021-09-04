from Analizadores.Sintactico import parser
from Analizadores.Sintactico import names

if __name__ == '__main__':
    f = open('Estudiantes.txt', "r", encoding="utf-8")
    mensaje = f.read()
    f.close()
    parser.parse(mensaje)

