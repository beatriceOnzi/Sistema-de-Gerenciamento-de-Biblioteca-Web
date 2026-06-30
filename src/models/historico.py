from . import db

class Historico(db.Model):
    __tablename__ = "historico"

    id = db.Column(db.Integer, primary_key=True)
    # id_emprestimo = db.Column(db.Integer, db.ForeignKey("emprestimo.id"))
    aluno_id = db.Column(db.Integer, db.ForeignKey("alunos.id"))
    livro_id = db.Column(db.Integer, db.ForeignKey("livros.id"))

    data_emprestimo = db.Column(db.Date)
    data_devolucao = db.Column(db.Date)

    turma = db.Column(db.Integer, db.ForeignKey("turma.turma"))
    
    # aluno = db.relationship("Aluno", backref="emprestimos")
    # livro = db.relationship("Livro", backref="emprestimos")