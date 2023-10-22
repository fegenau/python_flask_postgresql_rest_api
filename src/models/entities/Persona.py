class Persona():
    
    def __init__(self,id,nombre=None,usuario=None,contrasena=None,tipo=None,rut=None,email=None,carrera=None,apellidop=None)-> None:

        self.id=id
        self.nombre=nombre
        self.usuario=usuario
        self.contrasena=contrasena
        self.tipo=tipo
        self.rut=rut
        self.email=email
        self.carrera=carrera
        self.apellidop=apellidop
        
    def to_JSON(self):
        return {   
            'id': self.id,
            'nombre': self.nombre,
            'usuario': self.usuario,
            'contrasena': self.contrasena,
            'tipo': self.tipo,
            'rut': self.rut,
            'email':self.email,
            'carrera': self.carrera,
            'apellidop':self.apellidop,
        }