lista = []
menu = "pizza", "empanadas", "hamburguesa"
total= 0
while True:
    producto = input("que desea añadir a la lista? las opciones son pizza, hamburguesa o empanadas. (si desea salir, escriba -fin-): ")
    if producto == "fin":
        break
    if producto in menu:
        lista.append(producto)
        print("producto agregado con exito")
    else:
        print("lo sentimos el producto no es posible agregar, elija otra cosa")
    if producto == "pizza":
        total+=25
        #total= total + 25
    if producto == "hamburguesa":
        total+=30
        #total= total+30
    if producto == "empanadas":
        total+=20
        #total = total+20

print(f"su lista final es, {lista} con un precio de {total}$USD")
print("la cantidad de productos ingresados son: ")
print(len(lista))
input("presiona enter para salir")
