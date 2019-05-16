print ("Hola mundo")
print ("Feliz cumple, eu")
class Alumno (object):
    def __init__(self,nombre,apellido,DNI,matricula):
        self.nombre = nombre
        self.apellido = apellido
        self.DNI = DNI
        self.matricula = matricula
Mati = Alumno(Matias,Sendra,39888444,333)
print ("El DNI del alumno " + Mati.nombre + " es " + Mati.DNI)

