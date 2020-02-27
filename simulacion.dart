
import 'dart:math';

List<String> decisiones = ["si", "no"];
List<int> ganes = new List();

Random rnd = new Random();

int seleccionarPuerta(List<int> puertas) {
  int randomN = rnd.nextInt(3);
  return puertas[randomN];
}

int abrirPuerta(List<int> puertas, int posCoche, int seleccion) {
  int abrir = 1;
  while ((abrir == posCoche) || (abrir == seleccion)) {
    abrir = seleccionarPuerta(puertas);
  }
  return abrir;
}

String deseaCambiar(List<String> decisiones) {
  int randomN = rnd.nextInt(2);
  return decisiones[randomN];
}

int cambiarPuerta(List<int> puertas, int seleccion) {
  if (puertas.indexOf(seleccion) == 0) {
    return puertas[1];
  } else {
    return puertas[0];
  }
}

int simulaciones = 1000;

void main() {

  for (int i = 0; i < simulaciones; i++) {
    List<int> puertas = [1, 2, 3];
    print("Procesando iteración No. ${i+1}");

    int posCoche = seleccionarPuerta(puertas);
    int seleccion = seleccionarPuerta(puertas);

    int puertaAbierta = abrirPuerta(puertas, posCoche, seleccion);

    puertas.remove(puertaAbierta);

    //String decision = deseaCambiar(decisiones);
    String decision = "si";

    if (decision == "si") {
      seleccion = cambiarPuerta(puertas, seleccion);
    }

    if (seleccion == posCoche) {
      ganes.add(1);
    }
  }

  print("Cantidad de jugadas: $simulaciones\nCantidad de ganes: ${ganes.length}");
}