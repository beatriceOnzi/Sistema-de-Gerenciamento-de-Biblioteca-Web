from src.services.aluno_service import criar_aluno, deletar_aluno, validar_aluno, get_aluno_by_nome
from src.models.aluno import Aluno


def test_criar_criar_aluno(app):
    dados = {
        'nome': "Beatrice teste",
        'turma': 3
    }

    criar_aluno(dados)

    aluno_teste = Aluno.query.filter_by(
        nome="Beatrice teste"
    ).first()

    assert aluno_teste.nome == "Beatrice teste"
    assert aluno_teste.turma == 3


def test_get_aluno_por_nome(app):

    dados = {
        'nome': "Beatrice teste",
        'turma': 3
    }

    criar_aluno(dados)

    aluno_teste = get_aluno_by_nome("Beatrice teste")

    assert aluno_teste.nome == "Beatrice teste"
    assert aluno_teste.turma == 3


def test_deletar_aluno(app):
    dados = {
        'nome': "Beatrice teste",
        'turma': 3
    }

    criar_aluno(dados)
    aluno_teste = Aluno.query.filter_by(nome="Beatrice teste").first()

    assert aluno_teste is not None

    deletar_aluno(aluno_teste.id)
    aluno_deletado = Aluno.query.filter_by(nome="Beatrice teste").first()

    assert aluno_deletado is None

def test_validar_aluno_correto(app):
    dados = {
        'nome': "Beatrice teste",
        'turma': 3
    }
    erros = validar_aluno(dados)
    assert len(erros) == 0

def test_validar_aluno_muitos_caracteres(app):
    dados = {
        'nome': "Essa String tem mais de 120 caracteres At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium teste",
        'turma': 4
    }

    erros = validar_aluno(dados)
    assert "Digite um nome com menos de 120 caracteres" in erros

def test_validar_aluno_poucos_caracteres(app):
    dados = {
        'nome': "a",
        "turma": 4
    }

    erros = validar_aluno(dados)
    assert "Digite o nome completo do aluno" in erros

def test_validar_aluno_caracteres_proibidos(app):
    dados = {
        'nome': "Esse nome possui algo alem de letras $",
        "turma": 4
    }

    erros = validar_aluno(dados)
    assert "Digite apenas letras" in erros

def test_aluno_turma_invalida(app):
    dados = {
        'nome': "Nome Teste",
        "turma": 50
    }

    erros = validar_aluno(dados)
    assert "Turma inválida" in erros