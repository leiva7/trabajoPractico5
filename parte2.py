import numpy as np
import csv
with open("ecuacion.csv","r") as csvfile:
    recolector = csv.reader(csvfile, delimiter=",", quotechar='"')
    i = 0
    for linea in recolector:
        if i == 0:
            coef0 = int(linea[0])
            coef1 = int(linea[1])
            coef2 = int(linea[2])
            coef3 = int(linea[3])
            a = np.array([[coef0,coef1],[coef2,coef3]])
            i +=1
        if i == 1:
            coef4 = int(linea[0])
            coef5 = int(linea[1])
            b = np.array([coef4, coef5])
    print (np.linalg.solve(a,b))