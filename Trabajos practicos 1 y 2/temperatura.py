temperatura = int(input("que temperatura hay afuera?:"))
if temperatura < 0:
    print("se recomienda usar abrigo")
elif temperatura >0 and temperatura <20:
    print("se recomienda usar ropa mediana")
else:
    print("se recomienda usar ropa liviana")

input("si desea salir, presione enter")