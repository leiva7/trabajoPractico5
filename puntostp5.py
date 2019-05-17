#Creando el archivo para hacer las funciones

def esVocal(x):
    vocales = ["a","e","i","o","u"]
    if x in vocales:
        return "El caracter ingresado es vocal"
    else:
        return "El caracter ingresado es consonante o numero"

def sumaElementos(lista):
    resultado = 0
    for e in lista:
        resultado += e
    return resultado
    
def multiplicoelementos(lista):
    resultado = 1
    for e in lista:
        resultado = resultado*e
    return resultado
