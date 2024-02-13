class Persona:
    def __init__(self,DNI,nombre,apellidos,edad):
        self.DNI = DNI
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        print(f"La persona fue creada")

    def __str__(self):
        return f"{self.nombre} {self.apellidos} con DNI: {self.DNI} y {self.edad} años"
        
    def imprime(self):
        print(f"DNI: {self.DNI}\nNombre: {self.nombre} {self.apellidos}\nEdad: {self.edad}")

    def es_mayor_edad(self):
        if self.edad >= 18:
            print(True)
        else:
            print(False)

    def es_jubilado(self):
        if self.edad >= 65:
            print(True)
        else:
            print(False)

persona1 = Persona("12546465E","Azucena","Luján Garcia",15)
persona2 = Persona("54529984C","David","Escutia de Haro",19)
persona3 = Persona("54528964F","Julen","Agüero Fernandez",90)

persona3.imprime()
print()
persona1.es_mayor_edad()
persona2.es_mayor_edad()
print()
persona2.es_jubilado()
persona3.es_jubilado()