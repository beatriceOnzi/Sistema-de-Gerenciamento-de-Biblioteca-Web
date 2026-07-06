from src.services.turmas_service import get_turmas, adicionar_turmas
from src.models.turma import Turma


def test_get_turmas_retorna_todas_as_turmas_cadastradas(app):
    turmas = get_turmas()
    assert len(turmas) == 9


def test_adicionar_turmas_nao_duplica_turmas_existentes(app):
    adicionar_turmas()
    turmas = Turma.query.all()
    assert len(turmas) == 9


def test_turmas_sao_numeradas_de_1_a_9(app):
    turmas = get_turmas()
    numeros = sorted(t.turma for t in turmas)
    assert numeros == list(range(1, 10))
