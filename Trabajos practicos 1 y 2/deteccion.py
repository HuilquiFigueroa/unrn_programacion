numero = int(input("ingresa un numero:"))
#par o impar
if numero % 2 == 0: 
    print("es un numero par")
else:
    print("es un numero impar")
#menor, mayor o igual a 10
if numero < 10:
    print("el numero es menor a 10")
elif numero > 10:
    print("el numero es mayor a 10")
else:
    print("el numero es igual a 10")

input("si desea salir, presiona enter")
