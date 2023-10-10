from flask import Blueprint, jsonify, request

# models
from models.PersonaModel import PersonaModel

main = Blueprint('persona_blueprint', __name__)


@main.route('/')
def get_personas():
    try:
        persona=PersonaModel.get_personas()
        return jsonify(persona)
    except Exception as ex:    
        return jsonify({'message': str(ex)}),500


@main.route('/<string:usuario>')
def get_persona(usuario):
    try:
        persona=PersonaModel.get_persona(usuario)
        if persona!= None:
            return jsonify(persona)
        else:
            return jsonify({}),404
    except Exception as ex:    
        return jsonify({'message': str(ex)}),500



@main.route('/login', methods=['POST'])
def Post_login():
    usuario = request.json
    contraseña = request.json
    try:
        persona=PersonaModel.get_persona(usuario)
        if persona!= None:
            if persona['contraseña']==contraseña:
                return jsonify( {'mesagge':'Inicio de sesion exitoso', 'persona':persona.items}),200
                return
            else:
                return jsonify({'mesagge':'Credenciales invalidas'}),401
        else:
            return jsonify({}),404
    except Exception as ex:    
        return jsonify({'message': str(ex)}),500
   
