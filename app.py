from flask import Flask
from flasgger import Swagger
from app import routes
import os

def create_app():
    app = Flask(__name__)

    # Set correct database path
    app.config['DATABASE'] = os.path.join(app.root_path, 'database.db')

    # Swagger configuration
    Swagger(app)

    # Register blueprints or routes
    app.register_blueprint(routes.bp)

    # Clean DB connection on app context teardown
    from app.db import close_db
    app.teardown_appcontext(close_db)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
