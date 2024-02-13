number = 0
secret_number = 777
dificulty = 0
vidas = 0

print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|  Pero antes, escoge dificultad |
|      Facil: 10 vidas           |
|      Medio: 5 vidas            |
|      Dificil: 3 vidas          |
+================================+
""")

dificulty = input("Dificultad: ")
if dificulty == "facil":
    vidas = int(10)
elif dificulty == "medio":
    vidas = int(5)
else:
    vidas = int(3)

print("Has seleccionado el modo ", dificulty," y tienes ", vidas ," vidas, suerte",sep="")

number = int(input("Di un numero: "))

while number != secret_number and vidas != 0:
    vidas -= 1
    print("¡Ja, ja! ¡Estás atrapado en mi bucle y te quedan ", vidas , " vidas!",sep="")
    number = int(input("Di otro numero: "))

if vidas > 0:
    print ("¡Bien hecho, muggle! Eres libre ahora.")
else:
    print ("¡Te quedaste sin vidas! Has perdido.")