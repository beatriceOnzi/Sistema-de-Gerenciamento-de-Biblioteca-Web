from models import db, Livro

def get_livros():
    livro = Livro.query.order_by(Livro.nome).all()
    return livro

def novo_livro(titulo):
    novo_livro = Livro(nome=titulo)
    db.session.add(novo_livro)
    db.session.commit()

def delete_livro(id):
    livro = db.session.get(Livro, id)
    if livro:
        db.session.delete(livro)
        db.session.commit()