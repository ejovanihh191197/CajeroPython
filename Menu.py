import re

from Cuenta import Cuenta
from Generales import Generales


class Menu(Generales):
    nombre: str = ""
    pin: str
    intentos: int = 0

    def validarPin(self, pin: str):
        resultado: bool = True
        if pin == "12345":
            resultado = True
        else:
            resultado = False
            self.intentos += 1
        return resultado

    def validarNombre(self, nombre: str):
        res: bool = False
        p = re.compile('[A-Za-z ]{3,}')
        if p.match(nombre) is not None:
            res = True
        return res

    def validarCantidad(self, cantidad: str):
        res: bool = False
        p = re.compile('[0-9.]+')
        if p.match(cantidad) is not None:
            res = True
        return res

    def pedirDatos(self):
        temp: str = ""
        while self.nombre == "":
            print("\t.: Bienvenido :.")
            print("Por favor, ingrese su nombre y contraseña")
            temp = input("Nombre: ")
            if self.validarNombre(temp):
                self.nombre = temp
            else:
                print("Por favor, ingrese un nombre valido")
        self.pin = input("Ingresa el PIN: ")

    def opciones(self):
        retiro: float = 0.0
        opc:str = ""
        cuenta = Cuenta()
        while opc != "4":
            print("\t.: Bienvenido "+self.nombre + " :.")
            print("1.- Consultar saldo")
            print("2.- Retirar saldo")
            print("3.- Historial de movimientos")
            print("4.- Salir")
            print("Seleccionar opcion: ")
            opc = input()
            if opc == "1":
                cuenta.consultaSaldo()
                self.regresarMenu()
            elif opc == "2":
                cantidad: str =""
                while not(self.validarCantidad(cantidad)):
                    print("Hola "+self.nombre+" Ingresa la cantidad a retirar")
                    cantidad = input()
                    if self.validarCantidad(cantidad):
                        retiro = float(cantidad)
                        cuenta.retirar(retiro)
                    else:
                        print("Lo sentimos, ingrese una cantidad valida")
            elif opc == "3":
                if len(cuenta.getHistoria()) != 0:
                    print("========== Moviemientos ==========")
                    for x in cuenta.getHistoria():
                        print(x)
                    print("==================================")
                else:
                    print("No se cuentan con moviemientos hasta ahora")
                self.regresarMenu()
            elif opc == "4":
                print("Hasta pronto!!")
                exit(0)
            else:
                print("Ingresar una opcion valida, gracias")

    def principal(self):
        while self.intentos < 3:
            self.pedirDatos()
            if self.validarPin(self.pin):
                self.opciones()
                self.intentos = 4
            else:
                print("Intento fallido: " + str(self.intentos))
        if self.intentos == 3:
            print("Numero Maximo de intentos")
