class Vehiculo:
    color = ""
    ruedas = 0
    puertas = 0

class Coche(Vehiculo):
    velocidad = 0
    cilindrada = 0

c = Coche()
print(c.cilindrada)
print(c.ruedas)