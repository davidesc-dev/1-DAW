''' 
Descripción del programa: Se quiere realizar un programa que lea por
teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10).
A continuación debe mostrar todas las notas, la nota media, la nota más
alta que ha sacado y la menor.



Version: 1.0
Autor: David Escutia de Haro
''' 
#### Importar Librerias externas  #######
##### Declaración de Variables #######
nota = 0
notas = []
media = 0
minima = 0
maxima = 0
suma = 0


###### Fuciones y Procedimientos (Subprogramas) ######
###### Programa Principal #############
for i in range(5):
    nota = int(input(f"Introduzca la nota {i+1}/5: "))
    notas.append(nota)
minima = min(notas)
maxima = max(notas)
for i in range(5):
    suma += notas[i]
media = suma/5

print(f'''
   --NOTAS--
{notas}

-Minima: {minima}
-Maxima: {maxima}
-Media: {media}
''')