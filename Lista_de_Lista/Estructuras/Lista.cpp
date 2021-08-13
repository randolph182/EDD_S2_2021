#ifndef LISTA_H
#define LISTA_H

#include <stdlib.h>
#include <iostream>
#include "Nodo.cpp"
#include <typeinfo>

using namespace std;

template <typename T>
class Lista
{
private:
    /* data */
public:
    Nodo *primero;
    Nodo *ultimo;
    int size;
    Nodo * buscar(string _valor);
    Lista(/* args */);
    void insertar( T *_valor);
    
    void imprimir();
};

template <typename T>
Lista<T>::Lista(/* args */)
{
    this->primero = NULL;
    this->ultimo = NULL;
}

template <typename T>
                        //Carro 
void Lista<T>::insertar(T *_valor){
    if(this->primero == NULL){
        this->primero = _valor;
        this->ultimo = _valor;
        this->size++;
    }
    else if( dynamic_cast<Nodo*>(_valor)->toString() < this->primero->toString()){ //ESTRATEGIA DE INSERTAR AL INICIO
            
        this->primero->anterior = dynamic_cast<Nodo*>(_valor);
        dynamic_cast<Nodo*>(_valor)->siguiente = this->primero;
        this->primero = dynamic_cast<Nodo*>(_valor);

    }else if(dynamic_cast<Nodo*>(_valor)->toString()  > this->ultimo->toString()){ //ESTRATEGIA DE INSERTAR AL ULTIMO
        
        this->ultimo->siguiente = dynamic_cast<Nodo*>(_valor);
        dynamic_cast<Nodo*>(_valor)->anterior = this->ultimo;
        this->ultimo = dynamic_cast<Nodo*>(_valor);

    }else{ //SE BUSCA LA POSICION ADECUADA

        Nodo *tmp = this->primero;
        while(tmp->siguiente != NULL){
            //INSERCION AL MEDIO
            if (dynamic_cast<Nodo*>(_valor)->toString() > tmp->toString() and  dynamic_cast<Nodo*>(_valor)->toString() < tmp->siguiente->toString()){
                tmp->siguiente->anterior = dynamic_cast<Nodo*>(_valor);
                dynamic_cast<Nodo*>(_valor)->siguiente = tmp->siguiente;
                tmp->siguiente = dynamic_cast<Nodo*>(_valor);
                dynamic_cast<Nodo*>(_valor)->anterior = tmp;
            }
            tmp = tmp->siguiente;
        }
    }
}

template <typename T>
Nodo * Lista<T>::buscar(string _valor){
    // busqueda secuencial
   Nodo *tmp = this->primero;
   while (tmp != NULL)
   {
      if(tmp->toString() == _valor){
          return tmp;
      }
      tmp = tmp->siguiente;
   }
   return NULL;
}

template <typename T>
void Lista<T>::imprimir(){
   Nodo *tmp = this->primero;
   while (tmp != NULL)
   {
      cout << tmp->toString() << endl;
      tmp = tmp->siguiente;
   }
   
}


#endif