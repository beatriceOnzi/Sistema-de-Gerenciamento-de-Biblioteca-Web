import pytest

import src.services.aluno_service as service
import src.services.turmas_service as turmas_service
from src.repositories.aluno_repository import AlunoRepository

repo = AlunoRepository()


@pytest.fixture
def turmas(app):
    # validar_aluno consulta a tabela de turmas; get_turmas só cria se estiver vazia
    turmas_service.get_turmas()


def test_criar_aluno(app):
    dados = {'nome': "Beatrice teste", 'turma': 3}

    service.criar_aluno(dados)

    aluno_teste = repo.get_aluno_by_nome("Beatrice teste")
    assert aluno_teste.nome == "Beatrice teste"
    assert aluno_teste.turma == 3


def test_get_aluno_por_nome(app):
    repo.criar_aluno("Beatrice teste", 3)

    aluno_teste = service.get_aluno_by_nome("Beatrice teste")

    assert aluno_teste.nome == "Beatrice teste"
    assert aluno_teste.turma == 3


def test_get_alunos(app):
    repo.criar_aluno("Aluno Um", 2)
    repo.criar_aluno("Aluno Dois", 1)

    alunos = service.get_alunos()

    assert [a.nome for a in alunos] == ["Aluno Dois", "Aluno Um"]


def test_deletar_aluno(app):
    repo.criar_aluno("Beatrice teste", 3)
    aluno_teste = repo.get_aluno_by_nome("Beatrice teste")
    assert aluno_teste is not None

    service.deletar_aluno(aluno_teste.id)

    assert repo.get_aluno_by_nome("Beatrice teste") is None


def test_desativar_e_ativar_aluno(app):
    repo.criar_aluno("Beatrice teste", 3)
    aluno = repo.get_aluno_by_nome("Beatrice teste")

    service.desativar_aluno(aluno.id)
    assert service.status_aluno(aluno.id) is False

    service.ativar_aluno(aluno.id)
    assert service.status_aluno(aluno.id) is True


def test_existe_aluno(app):
    repo.criar_aluno("Beatrice teste", 3)
    aluno = repo.get_aluno_by_nome("Beatrice teste")

    assert service.existe_aluno(aluno.id) is True
    assert service.existe_aluno(9999) is False


def test_validar_aluno_correto(turmas):
    erros = service.validar_aluno({'nome': "Beatrice teste", 'turma': 3})

    assert erros == []


def test_validar_aluno_aceita_acentos(turmas):
    erros = service.validar_aluno({'nome': "José da Conceição", 'turma': 3})

    assert erros == []


def test_validar_aluno_muitos_caracteres(turmas):
    dados = {
        'nome': "Essa String tem mais de 120 caracteres At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium teste",
        'turma': 4
    }

    erros = service.validar_aluno(dados)

    assert "Digite um nome com menos de 100 caracteres" in erros


def test_validar_aluno_poucos_caracteres(turmas):
    erros = service.validar_aluno({'nome': "a", 'turma': 4})

    assert "Digite o nome completo do aluno" in erros


def test_validar_aluno_caracteres_proibidos(turmas):
    erros = service.validar_aluno({'nome': "Esse nome possui algo alem de letras $", 'turma': 4})

    assert "Digite apenas letras" in erros


def test_validar_aluno_turma_invalida(turmas):
    erros = service.validar_aluno({'nome': "Beatrice teste", 'turma': 99})

    assert "Turma inválida" in erros


def test_validar_aluno_ja_cadastrado(turmas):
    repo.criar_aluno("Beatrice teste", 3)

    erros = service.validar_aluno({'nome': "Beatrice teste", 'turma': 3})

    assert "Este aluno já está cadastrado" in erros


def test_validar_aluno_mesmo_nome_em_outra_turma_e_permitido(turmas):
    repo.criar_aluno("Beatrice teste", 3)

    erros = service.validar_aluno({'nome': "Beatrice teste", 'turma': 4})

    assert "Este aluno já está cadastrado" not in erros
