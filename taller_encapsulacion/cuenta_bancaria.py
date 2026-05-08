class CuentaBancaria:

    # Constructor
    def __init__(self, titular, saldo=0):

        self._titular = titular
        self._saldo = saldo

    # Property titular (solo lectura)
    @property
    def titular(self):
        return self._titular

    # Property saldo
    @property
    def saldo(self):
        return self._saldo

    # Setter saldo
    @saldo.setter
    def saldo(self, nuevo_saldo):

        if nuevo_saldo < 0:
            raise ValueError("El saldo no puede ser negativo")

        self._saldo = nuevo_saldo

    # Método depositar
    def depositar(self, cantidad):

        if cantidad > 0:
            self._saldo += cantidad
            return True

        return False

    # Método retirar
    def retirar(self, cantidad):

        if cantidad <= self._saldo:

            self._saldo -= cantidad
            return True

        return False


# Pruebas
def main():

    cuenta = CuentaBancaria("Kelly", 500000)

    print("Titular:", cuenta.titular)
    print("Saldo:", cuenta.saldo)

    # Depositar
    if cuenta.depositar(100000):
        print("Depósito exitoso")

    # Retirar
    if cuenta.retirar(200000):
        print("Retiro exitoso")

    print("Saldo actual:", cuenta.saldo)

    # Error saldo negativo
    try:
        cuenta.saldo = -5000

    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()
    