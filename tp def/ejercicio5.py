nota = float(input("coloque un numero: "))
def obtener_estado (nota):
    if nota >= 8:
        return "usted promociona "
    elif nota >=6 and nota <8:
        return "ustes esta aprobado "
    else:
        return "usted esta desaprobado "
resultado= (obtener_estado(nota))
print(resultado)

input("para salir presione enter ")


