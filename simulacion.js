
const decisiones = ['si', 'no']
let ganes = []

function randomNum(min, max) {
    return Math.floor(Math.random() * (max-min) + min)
}

function seleccionarPuerta(puertas) {
    let randomN = randomNum(0, 3)
    return puertas[randomN]
}

function abrirPuerta(puertas, posCoche, seleccion) {
    let abrir = 1
    while ((abrir === posCoche) || (abrir === seleccion)) {
        abrir = seleccionarPuerta(puertas)
    }
    return abrir
}

function deseaCambiar(decisiones) {
    let randomN = randomNum(0, 2)
    return decisiones[randomN]
}

function cambiarPuerta(puertas, seleccion) {
    if (puertas.indexOf(seleccion) == 0) {
        return puertas[1]
    } else {
        return puertas[0]
    }
}

const simulaciones = 1000

function main() {

    let posCoche, seleccion, puertaAbierta
    let puertas = []
    let decision

    for (var i = 0; i < simulaciones; i++) {
        puertas= [1, 2, 3]
        console.log(`Procesando iteración No. ${i+1}`)

        posCoche = seleccionarPuerta(puertas)
        seleccion = seleccionarPuerta(puertas)

        puertaAbierta = abrirPuerta(puertas, posCoche, seleccion)

        puertas.splice(puertas.indexOf(puertaAbierta), 1)

        // decision = deseaCambiar(decisiones)
        decision = 'si'

        if (decision === 'si') {
            seleccion = cambiarPuerta(puertas, seleccion)
        }

        if (seleccion == posCoche) {
            ganes.push(1)
        }
    }

    console.log(`\nCantidad de jugadas: ${simulaciones}\nCantidad de ganes: ${ganes.length}`)
}

main()