class Persona:

    def __init__(self, nombre, edad):

        self.nombre = nombre
        self.edad = edad

    def saludar(self):

        print(f"Hola, mi nombre es {self.nombre}")
        print(f"Tengo {self.edad} años")


# Crear objeto
persona1 = Persona("Kelly", 20)

# Llamar método
persona1.saludar()
