#include <stdlib.h>


template <typename T> 
class Nodo
{
    private:
        /* data */
        
    public:
        Nodo(T);
        T valor;
        Nodo * siguiente;

};

template <typename T>
Nodo<T>::Nodo(T val){
    this->siguiente = NULL;
    this->valor = val;
}