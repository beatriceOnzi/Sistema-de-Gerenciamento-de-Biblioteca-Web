from src.repositories.livro_repository import LivroRepository

livro_repository = LivroRepository()

def get_livros():
    livros = livro_repository.get_livros()
    return livros

def criar_livro(titulo):
    livro_repository.criar_livro(titulo)

def deletar_livro(id):
    livro_repository.deletar_livro(id)

def validar_livro(titulo):
    erros = []

    if len(titulo) >= 120:
        erros.append("Digite um título com menos de 120 caracteres")
    
    if len(titulo) <= 0:
        erros.append("Título inválido")
    
    return erros