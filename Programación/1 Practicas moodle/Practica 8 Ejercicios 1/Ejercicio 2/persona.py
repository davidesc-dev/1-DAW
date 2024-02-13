class Persona:
    def __init__(self,DNI,nombre,apellidos,edad):
        self.DNI = DNI
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        print(f"La persona fue creada")

    def __str__(self):
        if self.edad >= 18:
            return f"{self.nombre} {self.apellidos} con DNI: {self.DNI} es mayor de edad"
        else:
            return f"{self.nombre} {self.apellidos} con DNI: {self.DNI} no es mayor de edad"

persona1 = Persona("12546465E","Azucena","Luján Garcia",15)
persona2 = Persona("54529984C","David","Escutia de Haro",19)

print(persona1)
print()
print(persona2)