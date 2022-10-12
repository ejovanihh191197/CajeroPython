class Generales:
    opcion: str = ""
    salir: bool = True

    def regresarMenu(self):
        while self.salir:
            print("¿Que desea hacer?")
            print("1.- Regresar a menu principal")
            print("2.- Salir")
            opcion = input()
            if opcion == "1":
                self.salir = False
            elif opcion == "2":
                self.salir = False
                print("Hasta pronto!!")
                exit(0)
            else:
                print("Ingrese una opcion valida por favor")
