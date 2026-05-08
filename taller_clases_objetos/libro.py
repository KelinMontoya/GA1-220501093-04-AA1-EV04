# Clase Libro

class Libro:

    # Constructor
    def __init__(self, titulo, autor, paginas):

        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.disponible = True

    # Método prestar
    def prestar(self):

        if self.disponible:
            self.disponible = False
            return f"El libro '{self.titulo}' ha sido prestado."

        else:
            return f"El libro '{self.titulo}' no está disponible."

    # Método devolver
    def devolver(self):

        if not self.disponible:
            self.disponible = True
            return f"El libro '{self.titulo}' ha sido devuelto."

        else:
            return f"El libro '{self.titulo}' ya estaba en la biblioteca."

    # Método información
    def informacion(self):

        estado = "Disponible" if self.disponible else "Prestado"

        return f"""
Título: {self.titulo}
Autor: {self.autor}
Páginas: {self.paginas}
Estado: {estado}
"""


# Función principal
def main():

    # Crear objetos
    libro1 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 863)

    libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", 471)

    # Mostrar información
    print("=== INFORMACIÓN INICIAL ===")

    print(libro1.informacion())
    print(libro2.informacion())

    # Prestar libros
    print("=== PRÉSTAMO ===")

    print(libro1.prestar())
    print(libro2.prestar())

    # Intentar prestar nuevamente
    print("=== INTENTO DE PRÉSTAMO ===")

    print(libro1.prestar())

    # Mostrar información
    print("=== ESTADO ACTUAL ===")

    print(libro1.informacion())

    # Devolver libro
    print("=== DEVOLUCIÓN ===")

    print(libro1.devolver())

    # Intentar devolver otra vez
    print("=== INTENTO DE DEVOLUCIÓN ===")

    print(libro1.devolver())

    # Estado final
    print("=== ESTADO FINAL ===")

    print(libro1.informacion())
    print(libro2.informacion())


# Ejecutar programa
if __name__ == "__main__":
    main()
    