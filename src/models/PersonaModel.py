
from flask import jsonify, request
from flask_cors import CORS
from database.db import get_connection
from .entities.Persona import Persona


class PersonaModel():

    @classmethod
    def get_personas(self):
        try:
            connection = get_connection()
            personas = []

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, nombre, usuario, contraseña, tipo, rut, email FROM persona ORDER BY nombre ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    persona = Persona(
                        row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                    personas.append(persona.to_JSON())

            connection.close()
            return personas
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_persona(self, usuario):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, nombre, usuario, contraseña, tipo, rut, email FROM persona WHERE usuario = %s", (usuario,))
                row = cursor.fetchone()

                persona = None
                if row != None:
                    persona = Persona(
                        row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                    persona = persona.to_JSON()

            connection.close()
            return persona
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def post_login(self,usuario, password):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, nombre, usuario, contrasena, tipo, rut, email FROM persona WHERE usuario = %s AND contrasena = %s", (usuario, password))
                row = cursor.fetchone()
                persona = None
                if row != None:
                    persona = Persona(
                        row[0], row[1], row[2], row[3], row[4], row[5], row[6]
                        )
                    persona = persona.to_JSON()

            connection.close()
            return persona
        except Exception as ex:
            return jsonify({'error': str(ex)}), 500
