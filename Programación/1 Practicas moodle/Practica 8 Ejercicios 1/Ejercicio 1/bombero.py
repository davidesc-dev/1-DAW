class Bombero:
    def __init__(self,nombre,apellidos,edad,casado,especialista):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.casado = casado
        self.especialista = especialista
        print(f"El bombero {self.nombre} fue creado correctamente")

    def __str__(self):
        return f"Nombre: {self.nombre}\nApellidos: {self.apellidos}\nEspecialista: {self.especialista}"

bombero1 = Bombero("David","Escutia","19",False,True)

print(bombero1)