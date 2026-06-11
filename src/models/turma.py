from . import db

class Turma(db.Model):
    __tablename__ = "turma"

    turma = db.Column(db.Integer, primary_key=True)
    turma_formatada = db.Column(db.String)
    semana_atual = db.Column(db.Integer, default=1)