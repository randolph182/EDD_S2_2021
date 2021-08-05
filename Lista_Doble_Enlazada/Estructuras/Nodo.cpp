#ifndef NODO_H
#define NODO_H

#include <stdlib.h>

template <typename T>
class Nodo
{
private:
    /* data */
public:
    T valor;
    int id;
    Nodo * siguiente; 
    Nodo * anterior;
    Nodo(T _valor, int _id);
    ~Nodo();
};


template <typename T>
Nodo<T>::Nodo(T _valor,int _id)
{
    this->valor = _valor;
    this->siguiente = NULL;
    this->anterior = NULL;
    this->id = _id;
}

template <typename T>
Nodo<T>::~Nodo()
{
}

#endif // NODO_H