class Asistencia():
    
    def __init__(self,id,nombre_alumno=None,sigla=None)-> None:
        self.id=id
        self.nombre_alumno=nombre_alumno
        self.sigla=sigla

    def to_JSON(self):
        return {
            'id': self.id,
            'nombre_alumno': self.nombre_alumno,
            'sigla':self.sigla,
        }
