from datetime import datetime


# Clase Equipo
class Equipo:

    def __init__(self, nombre):

        self.nombre = nombre
        self.__disponible = True
        self.prestamos = []

    # Consultar disponibilidad
    def disponible(self):
        return self.__disponible

    # Prestar equipo
    def prestar(self):

        if self.__disponible:
            self.__disponible = False
            return True

        return False

    # Devolver equipo
    def devolver(self):

        if not self.__disponible:
            self.__disponible = True
            return True

        return False


# Clase Usuario
class Usuario:

    def __init__(self, nombre):

        self.nombre = nombre


# Clase Prestamo
class Prestamo:

    def __init__(self, usuario, fecha):

        self.usuario = usuario
        self.fecha = fecha

    def mostrar(self):

        return f"Usuario: {self.usuario} | Fecha: {self.fecha}"


# Diccionario principal
equipos = {

    "Laptop Dell": Equipo("Laptop Dell"),
    "Proyector Epson": Equipo("Proyector Epson"),
    "Tablet Samsung": Equipo("Tablet Samsung")
}


# Mostrar equipos
def mostrar_equipos():

    print("\n=== EQUIPOS ===")

    for nombre, equipo in equipos.items():

        estado = "Disponible" if equipo.disponible() else "Prestado"

        print(f"{nombre} --> {estado}")


# Registrar préstamo
def registrar_prestamo():

    mostrar_equipos()

    nombre_equipo = input("\nIngrese el equipo: ")

    if nombre_equipo in equipos:

        equipo = equipos[nombre_equipo]

        if equipo.disponible():

            usuario = input("Ingrese el usuario: ")

            fecha = datetime.now().strftime("%d/%m/%Y")

            nuevo_prestamo = Prestamo(usuario, fecha)

            equipo.prestamos.append(
                (nuevo_prestamo.usuario, nuevo_prestamo.fecha)
            )

            equipo.prestar()

            print("Préstamo registrado correctamente")

        else:
            print("El equipo ya está prestado")

    else:
        print("El equipo no existe")


# Devolver equipo
def devolver_equipo():

    nombre_equipo = input("Ingrese equipo a devolver: ")

    if nombre_equipo in equipos:

        equipo = equipos[nombre_equipo]

        if not equipo.disponible():

            equipo.devolver()

            print("Equipo devuelto correctamente")

        else:
            print("Ese equipo ya estaba disponible")

    else:
        print("Equipo no encontrado")


# Ver historial
def ver_historial():

    print("\n=== HISTORIAL ===")

    for nombre, equipo in equipos.items():

        print(f"\nEquipo: {nombre}")

        if equipo.prestamos:

            for usuario, fecha in equipo.prestamos:

                print(f"Usuario: {usuario} | Fecha: {fecha}")

        else:
            print("Sin préstamos registrados")


# Agregar equipo
def agregar_equipo():

    nombre = input("Ingrese nuevo equipo: ")

    if nombre not in equipos:

        equipos[nombre] = Equipo(nombre)

        print("Equipo agregado correctamente")

    else:
        print("Ese equipo ya existe")


# Menú principal
def menu():

    while True:

        print("""
======== SISTEMA DE PRÉSTAMOS ========

1. Ver equipos
2. Registrar préstamo
3. Devolver equipo
4. Ver historial
5. Agregar equipo
6. Salir
""")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_equipos()

        elif opcion == "2":
            registrar_prestamo()

        elif opcion == "3":
            devolver_equipo()

        elif opcion == "4":
            ver_historial()

        elif opcion == "5":
            agregar_equipo()

        elif opcion == "6":
            print("Programa finalizado")
            break

        else:
            print("Opción inválida")


# Ejecutar sistema
menu()
