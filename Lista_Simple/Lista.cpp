#include <stdlib.h>
#include <iostream>
#include "Nodo.cpp"

template <typename T>
class Lista
{
private:
    /* data */
public:
    Nodo<T> * primero;
    Nodo<T> * ultimo;
    Lista(/* args */);
    void insertar(T val);
    void imprimir();
};

template <typename T>
Lista<T>::Lista(/* args */)
{
    this->primero = NULL;
    this->ultimo = NULL;
}

template <typename T>
void Lista<T>::insertar(T val){
    Nodo<T> * nuevo = new Nodo<T>(val);

    if(this->primero == NULL){
        this->primero = nuevo;
        this->ultimo = nuevo;
    }else{
        this->ultimo->siguiente = nuevo;
        this->ultimo = nuevo;
    }
}

template <typename T>
void Lista<T>::imprimir(){
    Nodo<T> *tmp = this->primero;

    while (tmp != NULL)
    {
        std::cout << tmp->valor << std::endl;

        tmp = tmp->siguiente;
    }
    
}



