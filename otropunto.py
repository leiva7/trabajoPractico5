#Creando el archivo para hacer las funciones
def max2 (a,b):
    if a>b:
        return a
    elif a<b:
        return b

## maximo de tres numeros
def max3 (a,b,c):
    if a>b  and a>c:
        return a
    elif b>a and b>c:
        return b
    elif c>a and c>b:
        return c
    elif a==b==c:
        return "son iguales"
## largo de una lista


def largo (lista):
    resultado=0
    for elementos in lista:
        resultado += 1
    return resultado

        


