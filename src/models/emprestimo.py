from . import db
from sqlalchemy import func

class Emprestimo(db.Model):
    __tablename__ = "emprestimos"

    id = db.Column(db.Integer, primary_key=True)
    aluno_id = db.Column(db.Integer, db.ForeignKey("alunos.id"))
    livro_id = db.Column(db.Integer, db.ForeignKey("livros.id"))

    data_emprestimo = db.Column(db.Date, default=func.current_date())
    data_devolucao_prevista = db.Column(db.Date)
    data_devolucao = db.Column(db.Date)

    turma = db.Column(db.Integer)