#include <iostream>
#include <stdlib.h>
#include "../Estructuras/Nodo.cpp"
using namespace std;

class Persona : public Nodo
{
private:
    /* data */
public:
    string nombre;
    Persona(string);
    string toString();
    ~Persona();
};

Persona::Persona(string _nombre )
{
    this->nombre = _nombre;
}
    
Persona::~Persona()
{
}

string Persona::toString(){
    return this->nombre;
}
