#ifndef DIRECTORIO_H
#define DIRECTORIO_H
#include <iostream>
#include <stdlib.h>
#include "../Estructuras/Nodo.cpp"
#include "../Estructuras/Lista.cpp"

using namespace std;

class Directorio: public Nodo
{
private:
    /* data */
public:
    string letra;
    Lista<Nodo> *ptrContactos;
    Directorio(string);
    string toString();
    ~Directorio();
};

Directorio::Directorio(string _letra)
{
    this->letra = _letra;
    this->ptrContactos = new Lista<Nodo>();
}

string Directorio::toString(/* args */)
{
    return this->letra;
}


#endif
