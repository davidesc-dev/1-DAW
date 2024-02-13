class Colegio:

    alumnos = []
    profesores = []
    cursos = []

    def __init__(self,nombre,direccion,telefono,capacidad,director):
        self._nombre = nombre
        self._direccion = direccion
        self._telefono = telefono
        self._capacidad = capacidad
        self._director = director

        print(f"El colegio {self._nombre} ha sido creado")

    def __str__(self) -> str:
        return f"Colegio: {self._nombre}"
    
    def matricularAlumno(self,alumno):
        if len(self.alumnos) < self._capacidad:
            self.alumnos.append(alumno)
            print("El alumno fue matriculado")
        elif len(self.alumnos) >= self._capacidad:
            print("El alumno no pudo ser añadido porque el colegio no tiene mas capacidad")
        else:
            print("Se produjo un error al añadir al alumno")

    def eliminarAlumno(self,nalumno):
        nalumno = input("Introduzca el nombre del alumno a eliminar: ")
        for alumno in self.alumnos:
            if alumno == nalumno:
                self.alumnos.remove[alumno]
                print(f"Alumno {nalumno} eliminado setisfactoriamente")

    def eliminarAlumno2(self,nalumno):
        nalumno = input("Introduzca el nombre del alumno a eliminar: ")
        if nalumno in self.alumnos:
            if nalumno == nalumno:
                self.alumnos.remove[nalumno]
                print(f"Alumno {nalumno} eliminado setisfactoriamente")

    def mostrarAlumnos(self):
        print(f"El colegio {self._nombre} tiene los siguientes alumnos:")
        for alumno in self.alumnos:
            print(f"{alumno}")

    def contratarProfesor(self,profesor):
        profesor = input("Añadir profesor: ")
        self.profesores.append(profesor)

    def obtenerCursos(self):
        return self.cursos
    
    