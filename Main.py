class Alumno():
    nombre = None
    nota = None

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def aprueba(self, nota, nombre):
        if (nota >= 3.0):
            print("El estudiante", nombre, "ha aprobado el curso con una calificación de: ", nota)
        else:
            print("El estudiante", nombre, "no ha aprobado el curso con una calificación de: ", nota)


nombreAlumno = (input("Por favor ingrese el nombre del alumno: "))
notaAlumno=float(input("Por favor ingrese la nota del alumno: "))
a = Alumno(nombreAlumno,notaAlumno)
a.aprueba(a.nota, a.nombre)
