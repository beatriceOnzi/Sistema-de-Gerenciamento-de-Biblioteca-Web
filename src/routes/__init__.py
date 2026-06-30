from .aluno import bp as aluno_bp
from .livro import bp as livro_bp
from .turmas import bp as turmas_bp
from .emprestimos import bp as emprestimo_bp
from .historico import bp as historico_pb


def registrar_routes(app):
    app.register_blueprint(aluno_bp)
    app.register_blueprint(livro_bp)
    app.register_blueprint(emprestimo_bp)
    app.register_blueprint(turmas_bp)
    app.register_blueprint(historico_pb)