animales = []

class Mascotas(object):
    def __init__(self,nombre,edad,estado,fechaNacimiento):
        self.nombre = nombre
        self.edad = edad
        self.estado = estado
        self.fechaNacimiento = fechaNacimiento

    def muestra(self):
        print(f"Nombre: {self.nombre} - Tipo: {type(self.__class__.__name__)}")

    def cumpleaños(self):
        self.edad += 1
        print(f"{self.nombre} ha cumplido {self.edad} años!! 🎂🥳🎉🎉")

    def muestraconcreto(self):
        objeto = (input("Ingrese nombre: "))
        try:
            for animal in animales:
                if objeto == self.nombre:
                    print(f"Nombre: {self.nombre} - Tipo: {type(self.__class__.__name__)}")
        except:
            print(f"No se encontró ningun animal llamado {objeto}")

    def morir(self):
        print(f"{self.nombre} partió a un lugar mejor 🪦")

    def habla(self):
        print(f"*Gruñido*")


class Perro(Mascotas):
    def __init__(self,nombre,edad,estado,fechaNacimiento,raza,pulgas):
        super().__init__(nombre,edad,estado,fechaNacimiento)
        self.raza = raza
        self.pulgas = pulgas
        animales.append(self)
        print(f"✅ {self.nombre} añadido correctamente")

    def __str__(self):
        return f"Perro"
    
    def muestra(self):
        print(f"Nombre: {self.nombre} - Raza: {self.raza}")

    def habla(self):
        print("Gwoof guau wof")
    
class Gato(Mascotas):
    def __init__(self,nombre,edad,estado,fechaNacimiento,color,peloLargo):
        super().__init__(nombre,edad,estado,fechaNacimiento)
        self.color = color
        self.peloLargo = peloLargo
        animales.append(self)
        print(f"✅ {self.nombre} añadido correctamente")

    def __str__(self):
        return f"Gato."
    
    def muestra(self):
        print(f"Nombre: {self.nombre} - Color: {self.color}")

    def habla(self):
        print("Miau miau meew")

class Aves(Mascotas):
    def __init__(self,nombre,edad,estado,fechaNacimiento,pico,vuela):
        super().__init__(nombre,edad,estado,fechaNacimiento)
        self.pico = pico
        self.vuela = vuela
        animales.append(self)
        print(f"✅ {self.nombre} añadido correctamente")

    def volar():
        print("Flying 🪽🚁🪁🪁")

class Loro(Aves,Mascotas):
    def __init__(self,nombre,edad,estado,fechaNacimiento,pico,vuela,origen,habla):
        super().__init__(nombre,edad,estado,fechaNacimiento,pico,vuela)
        self.origen = origen
        self.habla = habla
        animales.append(self)
        print(f"✅ {self.nombre} añadido correctamente")

    def muestra(self):
        print(f"Nombre: {self.nombre} - Origen: {self.origen}")

    def saluda(self):
        print(f"Grr hola, me llamo {self.nombre} grrrr")

    def volar(self):
        print(f"{self.nombre} se fue a volar")

class Canario(Aves,Mascotas):
    def __init__(self,nombre,edad,estado,fechaNacimiento,pico,vuela,color,canta):
        super().__init__(nombre,edad,estado,fechaNacimiento,pico,vuela)
        # Mascotas().__init__(nombre,edad,estado,fechaNacimiento)
        # Aves().__init__(pico,vuela)
        self.color = color
        self.canta = canta
        animales.append(self)
        print(f"✅ {self.nombre} añadido correctamente")

    def muestra(self):
        print(f"Nombre: {self.nombre} - Color: {self.color}")

    def habla(self):
        print(f"Pio pio 🎶🎵🎶🎶")

    def volar(self):
        print(f"{self.nombre} se fue por la ventana")


# animal1 = Perro("Dobby",10,"mal",2014,"caniche",True)
# animal2 = Gato("Luna",2,"muy bien",2022,"gris",True)
# animal3 = Loro("Parry",3,"bien",2021,"picoso",True,"malasia",True)
# animal4 = Canario("Piolin",8,"regular",2016,"curvado",False,"amarillo",True)


# animal1.muestra()
# print()
# animal1.morir()
# print(animal1)
# animal1.muestra()
# animal3.muestra()
# animal4.muestra()
# animal4.habla()
# animal4.morir()
# hola=input("quien: ")
# Mascotas.muestraconcreto(hola)