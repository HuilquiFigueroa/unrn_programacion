lista = []
while True:
    producto = input("que desea añadir a la lista? (si desea salir, escriba -fin-): ")
    if producto == "fin":
        break
    lista.append(producto)
print("su lista final es", lista)
print("la cantidad de productos ingresados son: ")
print(len(lista))


