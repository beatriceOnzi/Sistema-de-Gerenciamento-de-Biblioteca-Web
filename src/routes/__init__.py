from .aluno import bp as aluno_bp
from .livro import bp as livro_bp
from .turmas import bp as turmas_bp
from .turma import bp as turma_bp

def registrar_routes(app):
    app.register_blueprint(aluno_bp)
    app.register_blueprint(livro_bp)
    app.register_blueprint(turma_bp)
    app.register_blueprint(turmas_bp)