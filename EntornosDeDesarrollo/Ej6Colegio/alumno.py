class Alumno:

    lista_cursos = []

    def __init__(self,id,nombre,apellido,fechanacimiento,curso,direccion,telefono,email,colegio):
        self._id = id
        self._nombre = nombre
        self._apellido = apellido
        self._fechanacimiento = fechanacimiento
        self._curso = curso
        self._direccion = direccion
        self._telefono = telefono
        self._email = email
        self.colegio = colegio

        print(f"El alumno {self._nombre} ha sido añadido con el ID: {self._id}")

    def __str__(self):
        return f"-Alumno: {self._nombre}\n-ID: {self._id}"
    
    # def inscribirCurso():
        

    def obtenerCursosInscritos(self):
        for curso in self.lista_cursos:
            print(f"- {curso}")