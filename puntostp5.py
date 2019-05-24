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
	
def palindromo(palabra):
    nuevapalabra = ""
    i= len(palabra)
    while i >0:
        nuevapalabra = nuevapalabra + palabra[i-1]
        i -= 1
        print (nuevapalabra)
    if palabra == nuevapalabra:
        return "Si es palindromo"
    else:
        return "No es palindromo"
