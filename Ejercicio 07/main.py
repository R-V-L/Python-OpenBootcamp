class Alumno:
    nombre = ""
    nota = 0

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def cambiarNota(self, nota):
        self.nota = nota

    def esAprobatorio(self):
        if self.nota >= 6:
            print("Aprobado")
        else:
            print("Reprobado")

a = Alumno("Ricardo", 60)
a.esAprobatorio()

a.cambiarNota(50)
a.esAprobatorio()