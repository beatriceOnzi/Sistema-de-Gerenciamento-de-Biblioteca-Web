from src.models import db, Livro

class LivroRepository:
    
    def get_livros(self):
        livros = Livro.query.order_by(Livro.nome).all()
        return livros

    def criar_livro(self, titulo):
        novo_livro = Livro(nome=titulo)
        db.session.add(novo_livro)
        db.session.commit()

    def deletar_livro(self, id):
        livro = db.session.get(Livro, id)
        if livro:
            db.session.delete(livro)
            db.session.commit()
        