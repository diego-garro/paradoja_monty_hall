
import random

puertas = [1, 2, 3]
pos_coche = random.choice(puertas)

print("Seleccione una puerta: ")
print("     [1]  [2]  [3]     ")
seleccion = int(input(": "))

def abrir(pos_coche, seleccion):
    global puertas
    abrir = 1
    while abrir == pos_coche or abrir == seleccion:
        abrir = random.choice(puertas)
    
    print("\nSe ha abierto la puerta No. {}\n".format(abrir))
    puertas.remove(abrir)

abrir(pos_coche, seleccion)

def cambiar():
    global seleccion
    if puertas.index(seleccion) == 0:
        return puertas[1]
    else:
        return puertas[0]
    

print("\nDesea cambiar de puerta? (s/n)")
respuesta = input(": ")
if respuesta.lower() == "s":
    seleccion = cambiar()
    print("Ahora tu puerta es la No. {}".format(seleccion))
else:
    print("Te quedaste con la puerta No. {}".format(seleccion))

print("\nEl coche está en la puerta No. {}".format(pos_coche))
if seleccion == pos_coche:
    print("FELICIDADES!! Ha ganado!!")
else:
    print("Lamentamos decirle que perdió!!")