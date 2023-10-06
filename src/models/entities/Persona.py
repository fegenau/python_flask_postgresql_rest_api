class Persona():
    def __init__(self,id,nombre=None,usuario=None,contraseña=None,tipo=None)-> None:
        self.id=id
        self.nombre=nombre
        self.usuario=usuario
        self.contraseña=contraseña
        self.tipo=tipo

    def to_JSON(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'usuario': self.usuario,
            'contraseña': self.contraseña,
            'tipo': self.tipo
        }