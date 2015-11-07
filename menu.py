# Definicion de salida de MENU
import sys
import time

from src import modules


def pMenu():
    time.sleep(1)
    print(30 * "-", "Bienvenido", 30 * "-")
    print("")
    print("\n")
    print("Seleccione Su opcion:\n")
    print("1.-Ruts")
    print("2.-Cb type")
    print("3.-Salir [X]")


def printMenu(menu):
    loop = True
    # Mientras se mantenga loop True
    while loop:
        pMenu()  # Despliega el menu
        opcion = input("\n ingrese su opcion [1-3] : ")

        if opcion == "1":
            print("Opcion 1 seleccionada \n")
            print("Se inicia el proceso de escritura en archivo......... \n")
            nombre = input("ingrese un nombre de archivo \n")
            print("El nombre ingresado es : " + nombre, end='\n')
            print("\n \n \n")
            mensaje = "Se procede a generar el diccionario de Ruts\n" \
                      "usted debe ingreasar el largo de la clave, considerando\n" \
                      "que se ha de agragar un digito extra como es el digito\n" \
                      "verificador, formato: [17382923] ... 8 digitos de largo\n" \
                      "maximo, de lo contrario de arrojará un error."

            print(mensaje)
            length = modules.readInt()
            if length > 8 or length <= 0:
                raise ValueError("Debe ingresar un valor valido")
                length = modules.readInt()
            print("Se inicia el proceso de escritura en archivo......... \n")
            print(100 * '-', end='\n')
            modules.writeFile(nombre, 4)
            print("Se ha finalizado el proceso, Enjoi :D", end='\n')
            print(100 * '-', end='\n')
            print("")
            time.sleep(1)
            print("Saliendo del sistema.....", end='\n')
            time.sleep(1)
            print("Adios")
            sys.exit(0)

        # cogigo de opcion 1
        elif opcion == "2":
            # codigo opcion 2
            print("Opcion 2 seleccionada")
        elif opcion == "3" or opcion == "q":
            print("Saliendo del Programa.... Adios ")
            sys.exit(0)
            loop = False
        else:
            # si ninguna opcion es seleccionada
            input("Wrong option selection. Enter to try again..")
            print("")
