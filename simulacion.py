
import random

decisiones = ["si", "no"]
ganes = []

def seleccionar_puerta():
    return random.choice(puertas)

def abrir(pos_coche, seleccion):
    abrir = 1
    while abrir == pos_coche or abrir == seleccion:
        abrir = random.choice(puertas)
    return abrir

def desea_cambiar():
    return random.choice(decisiones)

def cambiar():
    if puertas.index(seleccion) == 0:
        return puertas[1]
    else:
        return puertas[0]

simulaciones = 100

for i in range(simulaciones):
    
    puertas = [1, 2, 3]
    print("Procesando jugada No. {}".format(i+1))
    
    pos_coche = seleccionar_puerta()
    seleccion = seleccionar_puerta()
    puerta_abierta = abrir(pos_coche, seleccion)
    
    puertas.remove(puerta_abierta)
    
    #decision = desea_cambiar()
    decision = "si"
    
    if decision == "si":
        seleccion = cambiar()
    
    if seleccion == pos_coche:
        ganes.append(1)

print("Cantidad de jugadas: {}\nCantidad de ganes: {}".format(simulaciones, len(ganes)))
       