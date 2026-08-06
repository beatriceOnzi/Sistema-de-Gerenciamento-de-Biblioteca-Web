from flask import Flask
from flask_migrate import Migrate

from config import Config
from src.models import db
from src.routes import registrar_routes


def create_app(config_class=Config):
    app = Flask(
        __name__,
        template_folder="src/templates",
        static_folder="src/static"
    )

    app.config.from_object(config_class)

    db.init_app(app)
    
    Migrate(app, db)

    registrar_routes(app)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )