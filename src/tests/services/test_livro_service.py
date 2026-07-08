import src.services.livro_service as service
from src.repositories.livro_repository import LivroRepository

repo = LivroRepository()


def test_criar_novo_Livro(app):
    service.criar_livro("Livro teste")

    livro_teste = repo.get_livro_by_title("Livro teste")

    assert livro_teste.nome == "Livro teste"

def test_deletar_Livro(app):
    repo.criar_livro("Livro teste")
    livro_teste = repo.get_livro_by_title("Livro teste")

    assert livro_teste is not None

    service.deletar_livro(repo.get_id_by_title("Livro teste"))
    Livro_deletado = repo.get_livro_by_title("Livro teste")

    assert Livro_deletado is None

def test_validar_livro_correto(app):
    erros = service.validar_livro("Livro nome válido")
    assert len(erros) == 0

def test_validar_livro_muitos_caracteres(app):
    erros = service.validar_livro("Essa String tem mais de 120 caracteres At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium")
    assert "Digite um título com menos de 120 caracteres" in erros

def test_validar_livro_poucos_caracteres(app):
    erros = service.validar_livro("")
    assert "Título inválido" in erros
