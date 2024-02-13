class Galleta:
    chocolate = False
    sabor = "salado"
    color = "marron"

    def __init__(self, sabor, color):
        self.sabor = sabor
        self.color = color
        print("Galletita horneada")

    def __del__(self):
        print("La galleta fue tirada a la basura")

    def saludar(self):
        print("Hola soy una galleta")

    def chocolatear(self):
        self.chocolate = True

class Persona:
    pass


##### Programa Principal ######

una_galleta = Galleta("Dulce","Rosa")
otra_galleta = Galleta("Saladita","Marron")

# una_galleta.sabor = "salado"
# una_galleta.color = "marron"

print(f"El sabor de esta galleta es {una_galleta.sabor} y de color {una_galleta.color}")
print(f"El sabor de esta galleta es {una_galleta.sabor} y de color {una_galleta.color}")

persona1 = Persona()
persona2 = Persona()

print(una_galleta)
print(otra_galleta)
print(Galleta)
print("Pertenece a la clase",type(persona1).__name__)
print(type(persona1))

una_galleta.saludar()
print()
una_galleta.chocolatear()
print(una_galleta.chocolate)