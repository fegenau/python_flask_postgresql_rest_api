from flask import Flask

from config import config

# Routes
from routes import Persona

app = Flask(__name__) 


def page_not_found(error):
    return "<h1>Not found page</h1>",404


if __name__ == '__main__':
    app.config.from_object(config['development'])

    # Blueprints 
    app.register_blueprint(Persona.main, url_prefix='/api/persona')

    #Error handlers
    app.register_error_handler(404,page_not_found)
    app.run()
