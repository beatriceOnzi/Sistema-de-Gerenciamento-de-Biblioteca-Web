from src.models import db, Livro

def get_livros():
    livros = Livro.query.order_by(Livro.nome).all()
    return livros

def criar_livro(titulo):
    novo_livro = Livro(nome=titulo)
    db.session.add(novo_livro)
    db.session.commit()

def deletar_livro(id):
    livro = db.session.get(Livro, id)
    if livro:
        db.session.delete(livro)
        db.session.commit()

def validar_livro(titulo):
    erros = []

    if len(titulo) >= 120:
        erros.append("Digite um título com menos de 120 caracteres")
    
    if len(titulo) <= 0:
        erros.append("Título inválido")
    
    print(erros)
    
    return erros
    