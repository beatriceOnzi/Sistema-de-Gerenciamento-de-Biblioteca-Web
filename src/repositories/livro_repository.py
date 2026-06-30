from src.models import db, Livro

class LivroRepository:
    
    def get_livros(self):
        livros = Livro.query.order_by(Livro.nome).all()
        return livros
    
    def existe(self, titulo):
        return Livro.query.filter_by(nome=titulo).first() is not None

    def criar_livro(self, titulo):
        titulo = titulo.strip()
        novo_livro = Livro(nome=titulo)
        db.session.add(novo_livro)
        db.session.commit()

    def deletar_livro(self, id):
        livro = db.session.get(Livro, id)
        if livro:
            db.session.delete(livro)
            db.session.commit()
    
    def get_id_by_title(self, titulo):
        livro = Livro.query.filter_by(nome=titulo).first()

        if not livro:
            self.criar_livro(titulo)
            livro = Livro.query.filter_by(nome=titulo).first()

        return livro.id

        