import numpy as np

def saludar():
    print("Hola, estamos saludando desde saludos.saludar()")

def prueba():
    print("Esto es una NUEVA prueba de la nueva versión 6.0")

def generar_array(numeros):
    return np.arange(numeros)

class Saludo:
    def __init__(self):
        print("Hola, te saludo desde saludos.__init__")

if __name__ == '__main__':
    #saludar()
    print(generar_array(5))
