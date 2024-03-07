class Usuario():

    def __init__(self,nombre,email,telefono):
        self.nombre=nombre
        self.email=email
        self.telefono=telefono

    def __str__(self):
        return f"Usuario : {self.nombre} con email : {self.email} y telefono : {self.telefono}."
    
    def getEmail(self):
        return self.email
        