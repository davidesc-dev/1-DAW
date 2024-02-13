from profesor import *
from colegio import *
from alumno import *
from curso import *

colegio1 = Colegio("IES Abdera","Avenida de la guardia civil","1111111",10,"Lola Arroniz")

print(colegio1)

alumno1 = Alumno("1","David","Escutia","9/12/2004","1ª DAW","C/Maria Zambrano","675615812","david@gmail.com")

print(alumno1)

profesor1 = Profesor(1,"Daniel","Ruiz",675615817)

curso1 = Curso(1,"Bachillerato",1,"Ciencias")

colegio1.matricularAlumno(alumno1)
colegio1.mostrarAlumnos()