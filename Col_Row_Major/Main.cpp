#include <iostream>
#include <stdlib.h>
#include <sstream>

#include "./Objetos/Persona.cpp"

using namespace std;

int main(){
    int FILAS = 2;
    int COLS = 2;
    int LONG = 5;
    int CONT = 0;

    Persona  *chapines[FILAS][COLS][LONG];

    for (int i = 0; i < FILAS; i++)
    {
        for (int j = 0; j < COLS; j++)
        {
            for (int k = 0; k < LONG; k++)
            {
                stringstream nPersona;
                nPersona << CONT;

                stringstream ni;
                ni << i;

                stringstream nj;
                nj << j;

                stringstream nk;
                nk << k;

                chapines[i][j][k] = new Persona("Persona "+ nPersona.str(), ni.str() + "," + nj.str() + ","+nk.str());
                CONT++;
            }
            
        }
        
    }

    Persona *vectorChapin[FILAS * COLS * LONG];
    

    for (int i = 0; i < FILAS; i++)
    {
        for (int j = 0; j < COLS; j++)
        {
            for (int k = 0; k < LONG; k++)
            {
                //aplicando formula row major
                int pos = (i * COLS + j) * LONG + k;
                vectorChapin[pos] = chapines[i][j][k];
            }
        }
    }

    // for(Persona *persona: vectorChapin){
    //     cout << persona->nombre << " " << persona->dpi << endl;
    // }

    cout << vectorChapin[9]->nombre << " " << vectorChapin[9]->dpi << endl;


    system("pause");
    return 0;
}