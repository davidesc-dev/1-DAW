import mascota


animal1 = mascota.Perro("Dobby",10,"mal",2014,"caniche",True)
animal2 = mascota.Gato("Luna",2,"muy bien",2022,"gris",True)
animal3 = mascota.Loro("Parry",3,"bien",2021,"picoso",True,"malasia",True)
animal4 = mascota.Canario("Piolin",8,"regular",2016,"curvado",False,"amarillo",True)

animal1.muestra()
print()
animal1.morir()
print(animal1)
animal1.muestra()
animal3.muestra()
animal4.muestra()
animal4.habla()
animal4.morir()

print(mascota.animales)
