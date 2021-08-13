#include <iostream>
#include <stdlib.h>
#include "Controlador.cpp"


using namespace std;

int main(){
    Controlador *ctrl = new Controlador();
    ctrl->nuevo_directorio("b"); 
    ctrl->nuevo_directorio("a"); //insercion al inicio
    ctrl->nuevo_directorio("m"); //insercion al ultimo
    ctrl->nuevo_directorio("c"); //insercion al medio
    ctrl->nuevo_directorio("d"); //insercion al medio
    ctrl->nuevo_directorio("k"); 
    ctrl->nuevo_directorio("f"); 
    ctrl->imp_directorio();



    ctrl->nuevo_contacto("a","astro"); 
    ctrl->nuevo_contacto("a","ana"); 
    ctrl->imp_contacto("a");

    ctrl->nuevo_contacto("c","carlos"); 
    ctrl->nuevo_contacto("c","camilo"); 
    ctrl->imp_contacto("c");

    return 0;
}