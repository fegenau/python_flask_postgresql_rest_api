from flask import jsonify, request

from database.db import get_connection
from .entities.Asignatura import Asignatura 

class AsignaturaModel():

    @classmethod
    def get_asignatura(self):
        try:
            connection = get_connection()
            asignatura = []
            
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, nombre, sigla FROM asignatura ORDER BY nombre ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    asignatura = Asignatura(
                        row[0], row[1], row[2])
                    asignatura.append(asignatura.to_JSON())


            connection.close()
            return asignatura
        except Exception as ex:
            raise Exception(ex)
