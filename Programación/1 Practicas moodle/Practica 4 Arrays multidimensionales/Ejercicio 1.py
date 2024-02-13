'''
Descripción del programa: Diseñar el algoritmo correspondiente a un programa, que:
    ● Crea una tabla (lista con dos dimensiones) de 5x5 enteros.
    ● Carga la tabla con valores numéricos enteros.
    ● Suma todos los elementos de cada fila y todos los elementos de cada columna
      visualizando los resultados en pantalla.


Version: 1.0
Autor: David Escutia de Haro
''' 
#### Importar Librerias externas  #######
import random


##### Declaración de Variables #######
nrows = 5
ncols = 5
tabla = [[0 for row in range(nrows)] for col_ in range(ncols)]

###### Funciones y Procedimientos (Subprogramas) ######
###### Programa Principal #############
for row in range(nrows):
    for col in range(ncols):
        tabla[row][col] = random.randint(1, 10)

for row in tabla:
    print(row)    
      
suma_row = [sum(row) for row in tabla]
suma_col = [sum(tabla[i][j] for i in range(3)) for j in range(3)]

print("Suma de cada row:", suma_row)
print("Suma de cada col:", suma_col)