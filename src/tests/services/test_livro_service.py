from src.services.livro_service import criar_livro, deletar_livro, validar_livro
from src.models.livro import Livro


def test_criar_novo_Livro(app):

    criar_livro("Livro teste")

    livro_teste = Livro.query.filter_by(
        nome="Livro teste"
    ).first()

    assert livro_teste.nome == "Livro teste"

def test_deletar_Livro(app):
    criar_livro("Livro teste")
    livro_teste = Livro.query.filter_by(nome="Livro teste").first()

    assert livro_teste is not None

    deletar_livro(livro_teste.id)
    Livro_deletado = Livro.query.filter_by(nome="Livro teste").first()

    assert Livro_deletado is None

def test_validar_livro_correto(app):
    erros = validar_livro("Livro nome válido")
    assert len(erros) == 0

def test_validar_livro_muitos_caracteres(app):
    erros = validar_livro("Essa String tem mais de 120 caracteres At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium")
    assert "Digite um título com menos de 120 caracteres" in erros

def test_validar_livro_poucos_caracteres(app):
    erros = validar_livro("")
    assert "Título inválido" in erros
