class Animal:

    def __init__(self, especie):

        self.especie = especie

    def sonido(self):

        print(f"El {self.especie} hace un sonido")


animal1 = Animal("Perro")

animal1.sonido()
