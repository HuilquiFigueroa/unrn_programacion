def minutos_a_Segundos(minutos):
    return minutos * 60

try:
    minutos= int(input("ingresa_la_cantidad_de_minutos:"))
    if minutos < 0:
        print("por_favor_ingresa_numeros_positivos:")
    else:
        segundos = minutos_a_Segundos (minutos)
        print(f"{minutos} minutos son {segundos} segundos")
except ValueError:
    print("ingresa_numero_valido:")


input("si desea salir, presione enter")