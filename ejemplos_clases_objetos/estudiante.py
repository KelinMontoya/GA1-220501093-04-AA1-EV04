class Estudiante:

    def __init__(self, nombre, nota):

        self.nombre = nombre
        self.nota = nota

    def mostrar_nota(self):

        print(f"El estudiante {self.nombre} obtuvo {self.nota}")


estudiante1 = Estudiante("Juan", 4.5)

estudiante1.mostrar_nota()
