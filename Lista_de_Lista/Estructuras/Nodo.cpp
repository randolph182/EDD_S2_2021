#ifndef NODO_H
#define NODO_H

#include <iostream>
#include <stdlib.h>

using namespace std;


class Nodo
{
private:
    /* data */
public:
    Nodo * siguiente;
    Nodo * anterior;
    Nodo();
    virtual string toString() = 0;
};


Nodo::Nodo(/* args */)
{
    this->siguiente = NULL;
    this->anterior = NULL;
    // this->ptrLista = new Lista<Nodo>();
}



#endif