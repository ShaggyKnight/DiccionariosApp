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
        value = concatenarDigito(value)
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


def concatenarDigito(tuple):
    '''
    Concatena el digito verificador a una tupla
    :param tuple: tupla de comniantoria de numeros
    :return: tupla concatenada
    '''
    return tuple + (calculaDigito(number(tuple)),)


def number(numero):
    '''
    Concatena numeros en una lista, toma numeros, tuplas, listas, etc
    :param numero:
    :return: lista de numeros
    '''
    num = []
    for value in numero:
        num.append(value)
    return num


def calculaDigito(rut):
    '''
    Calcula el digito verificador de un rut dado.
    :param rut: representa un rut
    :return: digito verificador
    '''
    rut.reverse()
    recorrido = 2
    multiplicar = 0
    for x in rut:
        multiplicar += int(x) * recorrido
        if recorrido == 7: recorrido = 1
        recorrido += 1
    modulo = multiplicar % 11
    resultado = 11 - modulo
    if resultado == 11:
        digito = 0
    elif resultado == 10:
        digito = "K"
    else:
        digito = resultado
    return digito
