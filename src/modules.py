"""
author = eduardo

"""
import itertools


def combinaciones(rango):
    """

    :param rango: entero representando la cantidad maxima de numeros, rango > 0
    :return: combinatoria de numeros dado un rango
    """
    return itertools.product(range(1, rango + 1), repeat=rango)


def concatenate(*numeros):
    """
    :rtype: concatenacions de n numeros entregados por parametro, en un arreglo
    """
    salida = []
    for i in numeros:
        salida.append(i)
    return salida


def writeFile(name, lenght):
    """
    :param name: Nombre del archivo a escribir
    :param lenght: largo n 2^n combinaciones a escribirse
    :return:
    """
    file = open(name + ".lst", 'w')
    for value in combinaciones(lenght):
        # calcular y concatenar digito verificador y agregar ceros
        file.write('{0}\n'.format(''.join(map(str, value))))
    file.close()


def readInt():
    '''
    Solicita un valor entero, da 5 intentos para lograrlo
    :return: numero entero
    '''
    intentos = 0
    while intentos < 5:
        integer = input("Ingrese un numero: \n")
        try:
            integer = int(integer)
            return integer
        except ValueError:
            intentos += 1
            print("ATENCIÓN: Debe ingresar un número entero")
    raise (ValueError, "Valor incorrecto despues de 5 intentos")
