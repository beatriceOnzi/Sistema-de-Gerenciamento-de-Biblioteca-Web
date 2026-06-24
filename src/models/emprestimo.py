from . import db
from sqlalchemy import func
from datetime import date, timedelta

def calc_data_dev_prevista():
    return date.today() + timedelta(days=7)

class Emprestimo(db.Model):
    __tablename__ = "emprestimos"

    id = db.Column(db.Integer, primary_key=True)
    aluno_id = db.Column(db.Integer, db.ForeignKey("alunos.id"))
    livro_id = db.Column(db.Integer, db.ForeignKey("livros.id"))

    data_emprestimo = db.Column(db.Date, default=date.today)
    data_devolucao_prevista = db.Column(db.Date, default=calc_data_dev_prevista)
    data_devolucao = db.Column(db.Date)

    turma = db.Column(db.Integer, db.ForeignKey("turma.turma"))
    semana = db.Column(db.Integer, db.ForeignKey("turma.semana_atual"))
    
    aluno = db.relationship("Aluno", backref="emprestimos")
    livro = db.relationship("Livro", backref="emprestimos")