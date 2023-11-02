class Asignatura():
    
    def __init__(self,id,nombre=None,sigla=None)-> None:
        self.id=id
        self.nombre=nombre
        self.sigla=sigla

    def to_JSON(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'sigla':self.sigla,
        }
