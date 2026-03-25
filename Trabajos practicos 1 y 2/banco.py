contrasena_almacenada = 1234
clave_token = input("desea usar clave token? (si/no):")
if clave_token == "si":
    acceso_permitido = True 
    print("acceso permitido")
else:
    contrasena_ingresada = int(input("por favor ingresa una contrasena:"))
    if contrasena_ingresada == (contrasena_almacenada):
        print("acceso permitido")
    else:
        print("acceso denegado")

    

input("si desea salir, presiona enter")
