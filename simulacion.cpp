
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <string>
#include <ctime>

using namespace std;

vector<string> decisiones = {"si", "no"};
vector<int> ganes;

int seleccionarPuerta(vector<int> puertas) {
    int randomN = rand() % 3;
    return puertas[randomN];
}

int abrirPuerta(vector<int> puertas, int posCoche, int seleccion) {
    int abrir = 1;
    while ((abrir == posCoche) || (abrir == seleccion)) {
        abrir = seleccionarPuerta(puertas);
    }
    return abrir;
}

string deseaCambiar(vector<string> decisiones) {
    int randomN = rand() % 2;
    return decisiones[randomN];
}

int cambiarPuerta(vector<int> puertas, int seleccion) {
    if (puertas[0] == seleccion) {
        return puertas[1];
    } else {
        return puertas[0];
    }
}

template <typename T>
void removerElemento(vector<T>& vec, T elemento) {
    typename vector<T>::iterator it;
    for (it = vec.begin(); it <= vec.end(); it++) {
        if (*it == elemento) {
            vec.erase(it);
            break;
        }
    }
}

int simulaciones = 1000;

int main() {

    int posCoche, seleccion, puertaAbierta;
    vector<int> puertas;
    string decision;

    srand(time(0));

    for (int i = 0; i < simulaciones; i++) {

        puertas = {1, 2, 3};
        printf("Procesando iteración No. %3d\n", i+1);

        posCoche = seleccionarPuerta(puertas);
        seleccion = seleccionarPuerta(puertas);

        puertaAbierta = abrirPuerta(puertas, posCoche, seleccion);

        removerElemento(puertas, puertaAbierta);

        //decision = deseaCambiar(decisiones);
        decision = "si";

        if (decision == "si") {
            seleccion = cambiarPuerta(puertas, seleccion);
        }

        if (seleccion == posCoche) {
            ganes.push_back(1);
        }
    }

    printf("\nCantidad de jugadas: %5d \nCantidad de ganes: %5d\n", simulaciones, ganes.size());

    return 0;
}