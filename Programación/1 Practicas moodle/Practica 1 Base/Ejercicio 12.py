'''Descripción del programa:  Un alumno desea saber cuál será su calificación final en el módulo de Programación. Dicha calificación se compone de los siguientes porcentajes:
        55% del promedio de sus tres calificaciones parciales.
        30% de la calificación del examen final.
        15% de la calificación de un trabajo final. 


Version: 1.0
Autor: David Escutia de Haro
''' 
#### Importar Librerias externas  #######
##### Declaración de Variables #######
parc1 = 0
parc2 = 0
parc3 = 0
media_parc = 0
porcentaje_parc = 0
exam = 0
porcentaje_exam = 0
trab = 0
porcentaje_trab = 0
notafinal = 0


###### Fuciones y Procedimientos (Subprogramas) ######
###### Programa Principal #############
#Preguntas al usuario para recopilar las notas
parc1 = float(input("Introduzca la nota de su primer parcial: "))
parc2 = float(input("Introduzca la nota de su segundo parcial: "))
parc3 = float(input("Introduzca la nota de su tercer parcial: "))
exam = float(input("Introduzca la nota de su examen final: "))
trab = float(input("Introduzca la nota de su trabajo final: "))

#Operaciones del programa
media_parc = (parc1+parc2+parc3)/3
porcentaje_parc = (media_parc/100) * 55
porcentaje_exam = (exam/100) * 30
porcentaje_trab = (trab/100) * 15

#Cálculo de la nota final haciendo la suma de los porcentajes ya anteriormente calculados
notafinal = porcentaje_parc + porcentaje_exam + porcentaje_trab

#Mensaje al usuario con su nota final
print("Su nota del curso de programación es de:",notafinal)