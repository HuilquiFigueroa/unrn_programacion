nombres = [" mara ", "TOMAS", "  luCIA", "mARcos  ", " SOFIA "]
nombres_limpios = []

for nomb in nombres:
    name = nomb.strip().capitalize()
    nombres_limpios.append(name)

print(nombres_limpios)