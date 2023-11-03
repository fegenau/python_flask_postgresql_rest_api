
from flask import jsonify, request

from database.db import get_connection
from .entities.Persona import Persona
from .entities.Asignatura import Asignatura


class PersonaModel():

    @classmethod
    def get_personas(self):
        try:
            connection = get_connection()
            personas = []

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, nombre, usuario, contrasena, tipo, rut, email, carrera FROM persona ORDER BY nombre ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    persona = Persona(
                        row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
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
                    "SELECT id, nombre, usuario, contrasena, tipo, rut, email FROM persona WHERE usuario = %s", (usuario,))
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
                    "SELECT id, nombre, usuario, contrasena, tipo, rut, email, carrera, apellidop FROM persona WHERE usuario = %s AND contrasena = %s", (usuario, password))
                row = cursor.fetchone()
                persona = None
                if row != None:
                    persona = Persona(
                        row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8],
                        )
                    persona = persona.to_JSON()

            connection.close()
            return persona
        except Exception as ex:
            return jsonify({'error': str(ex)}), 500

    @classmethod
    def get_asignatura(self):
        try:
            # Establecer conexión con la base de datos
            connection = get_connection()
            asignaturas = []
            
            with connection.cursor() as cursor:
                # Ejecutar consulta SQL
                cursor.execute(
                    "SELECT id, nombre, sigla FROM asignatura ORDER BY nombre ASC")
                resultset = cursor.fetchall()

                # Iterar sobre los resultados y crear objetos Asignatura
                for row in resultset:
                    asignatura = Asignatura(
                        row[0], row[1], row[2])
                    asignaturas.append(asignatura.to_JSON())

            # Cerrar la conexión con la base de datos
            connection.close()
            return asignaturas
        except Exception as ex:
            # Lanzar la excepción para que pueda ser manejada en otra parte
            raise Exception(ex)

    @classmethod
    def post_asignatura(self,sigla):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, nombre, sigla FROM asignatura WHERE sigla = %s ", (sigla))
                row = cursor.fetchone()
                asignatura = None
                if row != None:
                    asignatura = Asignatura(
                        row[0], row[1], row[2]
                        )
                    asignatura = asignatura.to_JSON()

            connection.close()
            return asignatura
        except Exception as ex:
            return jsonify({'error': str(ex)}), 500
        
    @classmethod
    def get_asignatura(self, sigla):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, nombre, sigla FROM asignatura WHERE sigla = %s", (sigla))
                row = cursor.fetchone()

                asignatura = None
                if row != None:
                    asignatura = Asignatura(
                        row[0], row[1], row[2])
                    asignatura = asignatura.to_JSON()

            connection.close()
            return asignatura
        except Exception as ex:
            raise Exception(ex)