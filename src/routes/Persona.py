from flask import Blueprint, jsonify, request

# models
from models.PersonaModel import PersonaModel

main = Blueprint('persona_blueprint', __name__)


@main.route('/')
def get_personas():
    try:
        persona = PersonaModel.get_personas()
        return jsonify(persona)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/asignatura')
def get_asignatura():
    try:
        asignatura = PersonaModel.get_asignatura()
        return jsonify(asignatura)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500    


@main.route('/<string:usuario>')
def get_persona(usuario):
    try:
        persona = PersonaModel.get_persona(usuario)
        if persona != None:
            return jsonify(persona)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/login', methods=['POST'])
def post_login():
    usuario = request.json.get('usuario')
    password = request.json.get('password')
    try:
        persona = PersonaModel.post_login(usuario,password)
        
        return jsonify(persona)
        
    except Exception as ex:
        return jsonify({'message': str(ex)}), 501

