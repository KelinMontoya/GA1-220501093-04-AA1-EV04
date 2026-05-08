class Carro:

    def __init__(self, marca, color):

        self.marca = marca
        self.color = color

    def arrancar(self):

        print(f"El carro {self.marca} está arrancando")


# Crear objeto
carro1 = Carro("Toyota", "Rojo")

carro1.arrancar()
