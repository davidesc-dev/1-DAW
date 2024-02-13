'''
Descripción del programa: Un ciclista parte de una ciudad A a las HH horas,
MM minutos y SS segundos. El tiempo de viaje hasta llegar a otra ciudad B
es de T segundos. Escribir un algoritmo que determine la hora de llegada a
la ciudad B.



Version: 1.0
Autor: David Escutia de Haro
''' 
#### Importar Librerias externas  #######
##### Declaración de Variables #######
HH = 0
MM = 0
SS = 0
T = 0

Ts = 0
Tf = 0
HHf = 0
HHs = 0
MMf = 0
SSf = 0


###### Fuciones y Procedimientos (Subprogramas) ######
###### Programa Principal #############
HH = int(input(f"Introduzca la hora de salida [*HH*:MM:SS]: "))
MM = int(input(f"Introduzca los minutos de salida [{HH}:*MM*:SS]: "))
SS = int(input(f"Introduzca los segundos de salida [{HH}:{MM}:*SS*]: "))
T = int(input(f"La hora de salida sería a las {HH}:{MM}:{SS}, introduzca el tiempo de viaje en segundos: "))

Ts = HH * 3600 + MM * 60 + SS
Tf = Ts + T

HHf = (Tf // 3600) % 24
Tf %= 3600
MMf = Tf // 60
SSf = Tf % 60

print(f"La hora de llegada sería a las [{HHf}:{MMf}:{SSf}]")