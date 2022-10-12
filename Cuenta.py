from Generales import Generales
from Historia import Historia


class Cuenta(Generales):
    saldo: float = 1000.0
    historia: list = []

    def setSaldo(self, saldo: float):
        self.saldo = saldo

    def getSaldo(self):
        return self.saldo

    def getHistoria(self):
        return self.historia

    def setHistoria(self, historia: list):
        self.historia = historia

    def consultaSaldo(self):
        print("Tu saldo es de: $" + str(self.getSaldo()))
        self.regresarMenu()

    def retirar(self, retiro: float):
        if self.saldo - retiro >= 0:
            elemento = Historia(self.saldo, self.saldo - retiro)
            self.historia.append(elemento)
            self.setSaldo(self.saldo - retiro)
            print("Movimiento exitoso\nDetalles del movimiento:")
            print(elemento)
        else:
            print("Lo sentimos, no cuenta con los fondos suficientes, Saldo actual: " + str(self.getSaldo()))
        self.regresarMenu()
