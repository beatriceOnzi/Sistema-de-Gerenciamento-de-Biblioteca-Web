from . import db

class Historico(db.Model):
    __tablename__ = "historico"

    id = db.Column(db.Integer, primary_key=True)
    id_emprestimo = db.Column(db.Integer, db.ForeignKey("emprestimos.id"))
    
    nome = db.Column(db.String(100), nullable=False)
    livro = db.Column(db.String(100), nullable=False)

    data_emprestimo = db.Column(db.Date)
    data_devolucao = db.Column(db.Date)

    turma = db.Column(db.Integer, db.ForeignKey("turma.turma"))