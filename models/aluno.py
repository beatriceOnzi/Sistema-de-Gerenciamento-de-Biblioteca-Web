from . import db

class Aluno(db.Model):
    __tablename__ = "alunos"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), unique=True, nullable=False)
    turma = db.Column(db.Integer)
