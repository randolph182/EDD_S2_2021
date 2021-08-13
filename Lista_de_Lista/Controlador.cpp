#include <iostream>
#include <stdlib.h>
#include "./Estructuras/Lista.cpp"
#include "./Estructuras/Nodo.cpp"
#include "./Objetos/Directorio.cpp"
#include "./Objetos/Persona.cpp"


class Controlador
{
private:
    /* data */
public:
    Lista<Directorio> *lstDirectorio ; 
    Lista<Persona> *lstPersona;
    Controlador(/* args */);
    
    void nuevo_directorio( string );
    void nuevo_contacto(string, string);
    void imp_directorio( );
    void imp_contacto(string);
    ~Controlador();
};



Controlador::Controlador(/* args */)
{
    this->lstDirectorio = new Lista<Directorio>();
    this->lstPersona = new Lista<Persona>();
}

Controlador::~Controlador()
{
}


void Controlador::nuevo_directorio(string letra)
{
    Directorio *nuevo = new Directorio(letra);
    this->lstDirectorio->insertar(nuevo);
}

void Controlador::nuevo_contacto(string indice, string nombre)
{
    Persona *contacto = new Persona(nombre);
    // SACAMOS EL DIRECOTRIO CORRESPONDIENTE A LA LETRA 
    Directorio *dir = dynamic_cast<Directorio*>(this->lstDirectorio->buscar(indice));
    dir->ptrContactos->insertar(contacto);
}

void Controlador::imp_contacto(string indice)
{
    // SACAMOS EL DIRECOTRIO CORRESPONDIENTE A LA LETRA 
    Directorio *dir = dynamic_cast<Directorio*>(this->lstDirectorio->buscar(indice));
    dir->ptrContactos->imprimir();
}

void Controlador::imp_directorio()
{
    this->lstDirectorio->imprimir();
}

