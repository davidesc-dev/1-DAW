''' 
Descripción del programa: Programa que declare tres
listas 'lista1', 'lista2' y 'lista3' de cinco enteros
cada uno, pida valores para 'lista1' y 'lista2' y
calcule lista3=lista1+lista2.


Version: 1.0
Autor: David Escutia de Haro
''' 
#### Importar Librerias externas  #######
##### Declaración de Variables #######
lista1 = []
lista2 = []
lista3 = []


###### Fuciones y Procedimientos (Subprogramas) ######
###### Programa Principal #############
for i in range(5):
    lista1.append(int(input(f"Introduzca el numero {i+1}/5 de la lista 1: ")))
for i in range(5):
    lista2.append(int(input(f"Introduzca el numero {i+1}/5 de la lista 2: ")))
for i in range(5):
    lista3.append(lista1[i]+lista2[i])
print(f'''
{lista1}
+
{lista2}
=
{lista3}
''')