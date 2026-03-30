jugadores = [
    "messi",
    "neymar",
    "cristiano",
    "kaka",
    "maguire"
]
i = 0
pregunta = input("por favor ingrese un jugador: ")
encontrado = False

while i< len(jugadores):
    if pregunta == jugadores[i]:
        print("jugador registrado. ")
        print("su indice es", i+1)
        encontrado = True
        break
    i+=1

else:
    encontrado = False
    print("jugador no registrado")

input("presione -enter- para salir: ")