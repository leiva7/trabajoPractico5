# -*- coding: <utf-8> -*-
import puntostp5
import otropunto

while(True):
    print("""
            Seleccione una opcion:
            1-Determinar el maximo entre dos numeros
            2-Determinar el maximo entre tres numeros
            3-Determinar el largo de una cadena de texto
            4-Determinar si un caracter ingresado es vocal o consonante
            5-Realizar la suma de los elementos de una lista
            6-Realizar la multiplicacion de los elementos de una lista
            7-Verificar si dos listas tienen elementos en comun
            8-Verificar si una palabra ingresada es un palindromo
            9-Salir
            """)
    op= input()
    if op==1:
        print("Ingrese el primer numero")
        n1=input()
        print("Ingrese el segundo numero")
        n2=input()
        print(otropunto.max2(n1,n2))
    elif op==2:
        print("Ingrese el primer numero")
        n1=input()
        print("Ingrese el segundo numero")
        n2=input()
        print("Ingrese el tercer numero")
        n3=input()
        print(otropunto.max3(n1,n2,n3))
    elif op==3:
        print ("ingrese una cadena (entre comillas dobles)")
        lista=input()
        print(otropunto.largo(lista))
    elif op==4:
        print ("ingrese una letra (entre comillas dobles)")
        x=input()
        print(puntostp5.esVocal(x))
    elif op==5:
        print ("ingrese una lista de numeros (entre corchetes y separados por comas)")
        lista=input()
        print(puntostp5.sumaElementos(lista))
    elif op==6:
        print ("ingrese una lista de numeros (entre corchetes y separados por comas)")
        lista=input()
        print(puntostp5.multiplicoelementos(lista))
    elif op==7:
        print ("opcion 7")
    elif op==8:
        print ("opcion 8")
    elif op==9:
        exit()

