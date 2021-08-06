#ifndef PERSONA_H
#define PERSONA_H

#include <iostream>

using namespace std;

class Persona
{
private:
    /* data */
public:
    string nombre; 
    string dpi;
    Persona(/* args */);
    Persona(string, string);
    ~Persona();
};

Persona::Persona(/* args */)
{
}

Persona::Persona(string _nombre, string _dpi)
{
    this->nombre = _nombre; 
    this->dpi = _dpi;
}

Persona::~Persona()
{
}



#endif