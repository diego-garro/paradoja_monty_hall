package main

import (
	"fmt"
	"math/rand"
	"time"
)

func seleccionarPuerta(puertas []int) int {
	source := rand.NewSource(time.Now().UnixNano())
	rnd := rand.New(source)
	return puertas[rnd.Intn(3)]
}

func abrirPuerta(puertas []int, posCoche int, seleccion int) int {
	abrir := 1
	for {
		if abrir == posCoche || abrir == seleccion {
			abrir = seleccionarPuerta(puertas)
		} else {
			break
		}
	}

	return abrir
}

func deseaCambiar(decisiones []string) string {
	source := rand.NewSource(time.Now().UnixNano())
	rnd := rand.New(source)
	return decisiones[rnd.Intn(2)]
}

func cambiarPuerta(puertas []int, seleccion int) int {
	if puertas[0] == seleccion {
		return puertas[1]
	} else {
		return puertas[0]
	}
}

func removerElementoSlice(slice []int, elemento int) []int {
	newSlice := []int{}
	for _, v := range slice {
		if v != elemento {
			newSlice = append(newSlice, v)
		}
	}

	return newSlice
}

func main() {
	//decisiones := []string{"si", "no"}
	ganes := []int{}
	simulaciones := 10000
	puertas := []int{1, 2, 3}

	for i := 0; i < simulaciones; i++ {
		puertas = []int{1, 2, 3}
		fmt.Println("Procesando iteracion No.", i+1)

		posCoche := seleccionarPuerta(puertas)
		seleccion := seleccionarPuerta(puertas)

		puertaAbierta := abrirPuerta(puertas, posCoche, seleccion)

		puertas = removerElementoSlice(puertas, puertaAbierta)

		//decision := deseaCambiar(decisiones)
		decision := "si"

		if decision == "si" {
			seleccion = cambiarPuerta(puertas, seleccion)
		}

		if seleccion == posCoche {
			ganes = append(ganes, 1)
		}
	}

	fmt.Println("\nCantidad de jugadas:", simulaciones, "\nCantidad de ganes:", len(ganes))
}
