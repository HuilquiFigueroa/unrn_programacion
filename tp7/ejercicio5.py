#El programa tiene que validar que:
#tenga un solo guion -;
#la parte de la izquierda tenga solo letras;
#la parte de la derecha tenga solo numeros.

codigo_de_materia = input("ingrese un codigo de materia en formato xxxx-000: ")
letras =[]
numeros = []
if codigo_de_materia.count("-") == 1:
       letras , numeros = codigo_de_materia.split("-")
       if len(letras) == 4 and len(numeros) ==3:
              print(f"Perfecto, su codigo de materia es: {letras.upper()}-{numeros}")
else:
       print("codigo invalido se esperaba un formato XXXX-000")



