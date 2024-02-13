class Curso:

    alumnos = []
    _profesor = ""

    def __init__(self,id,nombre,etapa,nivel,modalidad):
        self._id = id
        self._nombre = nombre
        self._etapa = etapa
        self._nivel = nivel
        self._modalidad = modalidad
        print(f"Se ha creado el curso {self._etapa}º {self._nombre} {self._modalidad}")

    def __str__(self):
        return f"Curso: {self._nombre}"
    