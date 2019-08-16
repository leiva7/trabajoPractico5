# -*- coding: <utf-8> -*-
import hashlib
import linecache

while(True):
    print("""
            Seleccione una opcion:
            1-Registrar un usuario y contraseña
            2-Visualizar usuarios
            3-Visualizar contraseñas
            4-Simular loggin
            5-Salir
            """)
    op= input()
    if op=="1":
        print("Registre el nombre de usuario")
        usuario=input()
        f = open("usuarios.txt", "a+")
        f.write(usuario + "\n")
        f.close()
        print("Ingrese una contraseña")
        pas=hashlib.md5(input().encode())
        f = open("pass.txt", "a+")
        f.write(pas.hexdigest()+ "\n")
        f.close()
        print("Se almaceno contraseña para le usuarie ", usuario)
    elif op=="2":
        f = open("usuarios.txt", "r")
        for linea in f.readlines():
            print(linea)
        f.close()
    elif op=="3":
        f = open("pass.txt", "r")
        for linea in f.readlines():
            print(linea)
        f.close()
    elif op=="4":
        usuario = input("Ingrese nombre de usuario")
        n_linea = 0
        encontrado = False
        f = open("usuarios.txt","r")
        for linea in f.readlines():
            n_linea +=1
            if usuario == linea.rstrip():
            #se usa rstrip() para eliminar los espacios al final de la linea almacenada en el archivo antes de comparar
                encontrado = True
                f.close()
                pas = linecache.getline("pass.txt",n_linea)
                contra = hashlib.md5(input("Ingrese su contraseña").encode())
                if pas == (contra.hexdigest()+ "\n"):
                    print("Loggueo exitoso")
                    break
                else:
                    print("Contraseña incorrecta para el usuario seleccionado")
                    break
        if encontrado == False:
            print("El usuario no existe")
        
        
        
    elif op=="5":
        exit()
        

