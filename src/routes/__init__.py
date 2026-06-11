from .cadastro import bp as cadastro_bp
from .home import bp as home_bp
from .turma import bp as turmas_bp

def registrar_routes(app):
    app.register_blueprint(cadastro_bp)
    app.register_blueprint(turmas_bp)
    app.register_blueprint(home_bp)