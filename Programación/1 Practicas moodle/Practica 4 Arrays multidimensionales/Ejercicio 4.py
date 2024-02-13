'''
Descripción del programa: De una empresa de transporte se quiere guardar el nombre de los conductores que tiene, y
los kilómetros que conducen cada día de la semana.
Para guardar esta información se van a utilizar dos arreglos:
    ● Nombre: Lista para guardar los nombres de los conductores.
    ● kms: Tabla para guardar los kilómetros que realizan cada día de la semana.
Se quiere generar una nueva lista ("total_kms") con los kilómetros totales que realiza cada
conductor.
Al finalizar se muestra la lista con los nombres de conductores y los kilómetros que han
realizado.



Version: 1.0
Autor: David Escutia de Haro
''' 
#### Importar Librerias externas  #######
##### Declaración de Variables #######
nombre = []
kms = []
total_kms = []
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
nombres = []

###### Funciones y Procedimientos (Subprogramas) ######
###### Programa Principal #############

num_conductores = int(input("Ingrese el número de conductores: "))

for i in range(num_conductores):
    nombre_conductor = input(f"Ingrese el nombre del conductor {i + 1}: ")
    nombres.append(nombre_conductor)
    kms_conductor = []
    for dia in dias_semana:
        kms_dia = float(input(f"Ingrese los kilómetros para el {dia} del conductor {nombre_conductor}: "))
        kms_conductor.append(kms_dia)
    kms.append(kms_conductor)
total_kms = [sum(kms_conductor) for kms_conductor in kms]

print()
print("Resumen:")
for i in range(num_conductores):
    print(f"{nombres[i]}: {total_kms[i]} kilómetros en total.")