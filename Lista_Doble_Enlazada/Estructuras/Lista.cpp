#ifndef LISTA_H
#define LISTA_H

#include <iostream>
#include <stdlib.h>
#include "Nodo.cpp"

template <typename T>
class Lista
{
private:
    /* data */
public:
    Nodo<T> *primero;
    Nodo<T> *ultimo;
    int size;
    Lista(/* args */);
    void insertar( T _valor);
    // ~Lista();
};

template <typename T>
Lista<T>::Lista(/* args */)
{
    this->primero = NULL;
    this->ultimo = NULL;
    this->size = 0;
}

template <typename T> 
void Lista<T>::insertar(T _valor){
    Nodo<T> *nuevo = new Nodo<T>(_valor,0);
    if(this->primero == NULL){
        this->primero = nuevo;
        this->ultimo = nuevo;
        this->size++;
        nuevo->id = this->size;
    }else{
        nuevo->siguiente = this->primero;
        primero->anterior = nuevo;

        nuevo->anterior = this->ultimo;
        this->ultimo->siguiente = nuevo;

        this->ultimo = nuevo;
        this->size++;
        nuevo->id = this->size;
    }
}

// template <typename T> 
// Lista<T>::~Lista()
// {
// }



#endif 