from ABB import  ABB
from Grafo import  Grafo
from flask import Flask, jsonify, request

# app = Flask(__name__)
if __name__ == '__main__':
    arbol = ABB()
    grafo = Grafo()
    # arbol.insertar(2,"nombre 2")
    # arbol.insertar(1, "nombre 1")
    # arbol.insertar(3, "nombre 3")
    arbol.insertar(1, "nombre 1")
    arbol.insertar(2, "nombre 2")
    arbol.insertar(3, "nombre 3")
    arbol.insertar(4, "nombre 4")
    arbol.insertar(5, "nombre 5")
    arbol.insertar(6, "nombre 6")
    # arbol.insertar(7, "nombre 7")
    grafo.graficarArbol(arbol.raiz)
# arbol.enOrden()

# @app.route('/')
# def index():
#     return "Hola clase de lab EDD"
#
# @app.route('/estudiantes',methods=['GET'])
# def get():
#     return jsonify({"estudiantes":arbol.enOrden()})
#
# @app.route('/grafo',methods=['GET'])
# def graficar():
#     grafo.graficarArbol(arbol.raiz)
#     return jsonify({"status":"ok"})
#
# @app.route('/setEstudiantes', methods=['POST','GET'])
# def pos():
#     if request.method == 'POST':
#         x = request.json
#         arbol.insertar( x['id'], x['nombre'])
#         return jsonify({"estudiantes":arbol.enOrden()})
#
#     return jsonify({'status': "bad"})
#
# if __name__ == '__main__':
#     app.run(debug=True)
