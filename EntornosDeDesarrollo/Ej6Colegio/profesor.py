class Profesor:
    def __init__(self,id,nombre,apellidos,telefono):
        self._id = id
        self._nombre = nombre
        self._apellidos = apellidos
        self._telefono = telefono
        print(f"Se ha creado el profesor {self._nombre}")

    def __str__(self) -> str:
        return f"Profesor: {self._nombre}"
