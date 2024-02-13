''' Descripción del programa: Pide al usuario dos pares de números x1,y2 y x2,y2, 
    que representen dos puntos en el plano. Calcula y muestra la distancia entre ellos.


    Version: 1.0
    Autor: David Escutia de Haro
''' 
#### Importar Librerias externas  #######


##### Declaración de Variables #######
x1 = 0
x2 = 0
y1 = 0
y2 = 0
dist_x = 0
dist_y = 0


###### Fuciones y Procedimientos (Subprogramas) ######



###### Programa Principal #############
x1 = int(input("Introduce una primera coordenada para X: "))        
x2 = int(input("Introduce una segunda coordenada para X: "))
y1 = int(input("Introduce una primera coordenada para Y: "))
y2 = int(input("Introduce una segunda coordenada para Y: "))

dist_x = abs(x1-x2)
dist_y = abs(x1-x2)

print("Valores introducidos x1:",x1," x2:",x2," y1:",y1," y2:",y2, sep="")
print("La distancia es de",dist_x,"en el eje X, y de",dist_y,"en el eje Y")