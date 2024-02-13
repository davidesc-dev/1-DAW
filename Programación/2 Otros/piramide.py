'''
Descripción del programa: Programa que lee la cantidad de bloques que tienen los constructores,
y genera la altura de la pirámide que se puede construir utilizando estos bloques.


Version: 1.0
Autor: David Escutia de Haro
''' 
#### Importar Librerias externas  #######
##### Declaración de Variables #######
blocks = int(input("Ingresa el número de bloques: "))           # Se declara una variable para los bloques totales disponibles
row = 1                                                         # Se declara la variable de las filas como 1 ya que la primera fila tiene 1 bloque
height = 0                                                      # Declaracion de la variable de la altura


###### Fuciones y Procedimientos (Subprogramas) ######
###### Programa Principal #############
while blocks > row:                                             # Bucle de los bloques totales, se van restando los que van siendo utilizados para las filas
    blocks -= row                                               # por lo que se va restando de la variable blocks, cada ciclo suma 1 a la altura y declara el
    height += 1                                                 # valor de la fila siguiente haciendola un bloque mas larga. En el momento que el numero de 
    row += 1                                                    # bloques restantes deja de ser mayor que los bloques necesarios para cada fila, significa que
                                                                # no hay suficiente para construir una fila mas, por lo que se sale del bucle dando la altura.
print("La altura de la pirámide:", height)