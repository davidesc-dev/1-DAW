'''
Descripción del programa: Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos)
después de pedirnos cuantas monedas tenemos (de 2€, 1€, 50 céntimos, 20 céntimos o 10 céntimos).


Version: 1.0
Autor: David Escutia de Haro
''' 
#### Importar Librerias externas  #######
##### Declaración de Variables #######
eur2 = 0
eur1 = 0
cent50 = 0
cent20 = 0
cent10 = 0
exceso_cents = 0
tot_eur = 0
tot_cent = 0

###### Fuciones y Procedimientos (Subprogramas) ######
###### Programa Principal #############
eur2 = int(input("Introduzca la cantidad de monedas de 2€: "))
eur1 = int(input("Introduzca la cantidad de monedas de 1€: "))
cent50 = int(input("Introduzca la cantidad de monedas de 50 céntimos: "))
cent20 = int(input("Introduzca la cantidad de monedas de 20 céntimos: "))
cent10 = int(input("Introduzca la cantidad de monedas de 10 céntimos: "))
tot_cent = (cent50*50 + cent20*20 + cent10*10)%100
exceso_cents = (cent50*50 + cent20*20 + cent10*10)//100
tot_eur = (eur2*2 + eur1 + exceso_cents)

print(f"Esas monedas suman un total de {tot_eur}€ y {tot_cent} céntimos")
