from flask import Flask
from flasgger import Swagger
from app.routes import api_bp
import os

def create_app():
    app = Flask(__name__)
    app.config['DATABASE'] = os.path.join(app.instance_path, 'database.db')
    app.config['SWAGGER'] = {
        'title': 'A swagger API',
        'uiversion': 3
    }

    os.makedirs(app.instance_path, exist_ok=True)

    Swagger(app)
    app.register_blueprint(api_bp)

    return app



