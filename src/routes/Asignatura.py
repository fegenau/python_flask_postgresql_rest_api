from flask import Blueprint, jsonify, request

# models
from models.AsignaturaModel import AsignaturaModel

main = Blueprint('asignatura_blueprint', __name__)


@main.route('/asignatura')
def get_asignatura():
    try:
        asignatura = AsignaturaModel.get_asignatura()
        return jsonify(asignatura)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500