#include <stdlib.h>
#include <iostream>

using namespace std;

class Objeto{
  public:
    string nombre;  
};

void modificar(Objeto *obj);
void modificar2(Objeto **obj);

int main(){
    Objeto *obj = new Objeto();
    obj->nombre = "hola mundo";

    modificar(&*obj);
    modificar2(&obj);
    cout << obj->nombre << endl;


    int a = 5; 
    int *aa = &a;
    int **aaa = &aa;
    **aaa = 10;
    cout << a << endl;
    return 0;
}


void modificar(Objeto *obj){
    obj->nombre = "Modificado de la primera forma";
}

void modificar2(Objeto **obj){
    (*obj)->nombre = "Modificado de la segunda forma";
}