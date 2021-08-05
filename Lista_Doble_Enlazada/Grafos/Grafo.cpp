#include <iostream>
#include <sstream>
#include <fstream>
#include "../Estructuras/Lista.cpp"

using namespace std;

template <typename T>
class Grafo
{
private:
    /* data */
public:
    Grafo(/* args */);
    void generarGrafo(Lista<T> *lista);
    string dirToString(Nodo<T> *valor);
    string valrToString(T valor);
};

template <typename T>
Grafo<T>::Grafo(/* args */)
{

}

template <typename T> 
void Grafo<T>::generarGrafo(Lista<T> *lista){
    string acum = "digraph G{\n rankdir = LR; \nnode [shape=box]; \ncompound=true; \n";
    string nodo = "";
    string enlace = "";

    Nodo<T> *tmp = lista->primero;
    while(tmp->siguiente != lista->primero){
        string hex = dirToString(&*tmp); 
        nodo += "\"" + hex + "\"" + "[label=\"" + valrToString(tmp->valor) + "\"];\n";
        enlace += "\"" +  dirToString(&*tmp) + "\" -> \"" + dirToString(&*(tmp->siguiente)) + "\"[dir=\"both\"];\n";
        tmp = tmp->siguiente;
    }
    //estamos en el ulitmo nodo
    nodo += "\"" + dirToString(&*tmp) + "\"[label=\"" + valrToString(tmp->valor) + "\"];\n";
    enlace += "\"" +  dirToString(&*tmp) + "\" -> \"" + dirToString(&*(tmp->siguiente)) + "\"[dir=\"both\"];\n";
    acum += nodo + enlace + "\n}\n";

    string filename("g.dot");
    fstream file_out;

    file_out.open(filename, std::ios_base::out);
    if(!file_out.is_open()){
        cout << "Error al abrir el archivo: " <<filename << '\n';
    }else{
        file_out << acum << endl;
        cout << "La escritura fue un exito" << endl;
    }

    string cmd = "dot -Tpng g.dot -o g.png";
    system(cmd.c_str());    
}

template <typename T> 
string Grafo<T>::dirToString(Nodo<T> *valor){
    stringstream ss; 
    ss << &*valor;
    return ss.str();
}

template <typename T> 
string Grafo<T>::valrToString(T valor){
    stringstream ss; 
    ss << valor;
    return ss.str();
}


