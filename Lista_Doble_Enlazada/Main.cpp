#include <iostream>
#include <stdlib.h>
#include "./Estructuras/Lista.cpp"
#include "./Grafos/Grafo.cpp"

using namespace std;

int main() {
    Lista<int> *lst = new Lista<int>();

    lst->insertar(1);
    lst->insertar(2);
    lst->insertar(3);
    lst->insertar(4);
    lst->insertar(5);
    lst->insertar(6);
    lst->insertar(7);
    lst->insertar(8);
    lst->insertar(9);
    lst->insertar(10);
    
    Grafo<int> *g  = new Grafo<int>();
    g->generarGrafo(&*lst);
    std::cout<< lst->size <<std::endl;

    // int a = 5;
    // cout << a << endl; 
    // int *aa = &a;

    // *aa = 6;

    // cout << a << endl;


    return 0;

    
}