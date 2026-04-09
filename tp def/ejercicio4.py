numero = float(input("por favor ingrese un numero: "))
porcentaje= 10
def calcular_descuento (precio):
    if precio > 10000:
        descuento = precio * (porcentaje/100)
        precio_final = precio - descuento
        return precio_final 
    else:
        return precio
resultado = (calcular_descuento(numero))
if numero > 10000:
    print("se aplico descuento del 10%", resultado)
else:
    print("no se aplico descuento", resultado)

input("presione enter para salir: ")








