class Persona():
    def __init__(self,id,nombre=None,usuario=None,contraseña=None,tipo=None,rut=None,email=None)-> None:

        self.id=id
        self.nombre=nombre
        self.usuario=usuario
        self.contraseña=contraseña
        self.tipo=tipo
        self.rut=rut
        self.email=email
        
    def to_JSON(self):
        return {   
            'id': self.id,
            'nombre': self.nombre,
            'usuario': self.usuario,
            'contraseña': self.contraseña,
            'tipo': self.tipo,
            'rut': self.rut,
            'email':self.email
        }