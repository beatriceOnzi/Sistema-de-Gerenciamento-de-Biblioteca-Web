from . import db

class Livro(db.Model):
    __tablename__ = "livros"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), unique=True, nullable=False)