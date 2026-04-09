def pedido_de_comida():
    comidas = input("que comida desea pedir: ").lower().strip()
    if comidas == "hamburguesa":
        print("perfecto su hamburguesa a sido añadido ")
    elif comidas == "pizza":
        print("perfecto su pizza a sido añadida ")
    elif comidas == "empanadas":
        print("perfecto sus empanadas fueron añadidas ")
    else:
        print("lo sentimos no contamos con esa comida el dia de hoy ")
    return comidas
comida = pedido_de_comida()
import preciocomidas
print(preciocomidas.precios(comida))

input("presione enter para salir: ")