lista = []
while len(lista) <5:
    producto = input("que desea añadir a la lista? (si desea salir, escriba -fin-): ")
    if producto == "fin":
        break
    lista.append(producto)
print("la lista final es de:", lista)
print("la cantidad de productos ingresados son: ")
print(len(lista))
