edad = input("ingrese su edad: ")
if edad.isnumeric():
    edad = int(edad)
    if edad >=0 and edad <=120:
        print(f"edad correcta ingresada: {edad}")
    else:
        print("numero incorrecto se espera un numero del 0 al 120")
elif edad.isalpha():
    print("datos ingresados incorrectos (se esperaban numeros)")
else:
    print("numero incorrecto se espera un numero del 0 al 120")
