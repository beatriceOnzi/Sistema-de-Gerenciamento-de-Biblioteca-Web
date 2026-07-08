import src.services.aluno_service as service
from src.repositories.aluno_repository import AlunoRepository

repo = AlunoRepository()


def test_criar_criar_aluno(app):
    dados = {
        'nome': "Beatrice teste",
        'turma': 3
    }

    service.criar_aluno(dados)

    aluno_teste = repo.get_aluno_by_nome("Beatrice teste")

    assert aluno_teste.nome == "Beatrice teste"
    assert aluno_teste.turma == 3


def test_get_aluno_por_nome(app):
    repo.criar_aluno("Beatrice teste", 3)

    aluno_teste = service.get_aluno_by_nome("Beatrice teste")

    assert aluno_teste.nome == "Beatrice teste"
    assert aluno_teste.turma == 3


def test_deletar_aluno(app):
    repo.criar_aluno("Beatrice teste", 3)
    aluno_teste = repo.get_aluno_by_nome("Beatrice teste")

    assert aluno_teste is not None

    service.deletar_aluno(aluno_teste.id)
    aluno_deletado = repo.get_aluno_by_nome("Beatrice teste")

    assert aluno_deletado is None

def test_validar_aluno_correto(app):
    dados = {
        'nome': "Beatrice teste",
        'turma': 3
    }
    erros = service.validar_aluno(dados)
    assert len(erros) == 0

def test_validar_aluno_muitos_caracteres(app):
    dados = {
        'nome': "Essa String tem mais de 120 caracteres At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium teste",
        'turma': 4
    }

    erros = service.validar_aluno(dados)
    assert "Digite um nome com menos de 100 caracteres" in erros

def test_validar_aluno_poucos_caracteres(app):
    dados = {
        'nome': "a",
        "turma": 4
    }

    erros = service.validar_aluno(dados)
    assert "Digite o nome completo do aluno" in erros

def test_validar_aluno_caracteres_proibidos(app):
    dados = {
        'nome': "Esse nome possui algo alem de letras $",
        "turma": 4
    }

    erros = service.validar_aluno(dados)
    assert "Digite apenas letras" in erros

def test_aluno_turma_invalida(app):
    dados = {
        'nome': "Nome Teste",
        "turma": 50
    }

    erros = service.validar_aluno(dados)
    assert "Turma inválida" in erros