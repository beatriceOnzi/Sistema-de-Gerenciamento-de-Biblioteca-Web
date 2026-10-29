from flask import Flask, send_from_directory
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

    with app.app_context():
        db.create_all()

    @app.route("/sw.js")
    def service_worker():
        resp = send_from_directory(app.static_folder, "sw.js")
        resp.headers["Cache-Control"] = "no-cache"
        resp.headers["Service-Worker-Allowed"] = "/"
        return resp

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0")