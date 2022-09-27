peso = int(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

indice_masa_corporal = peso / (altura ** 2)

print(round(indice_masa_corporal, 2))