from src.repositories.turmas_repository import TurmasRepository
from src.models.turma import Turma

repo = TurmasRepository()


def test_get_turmas_retorna_todas_as_turmas(app):
    turmas = repo.get_turmas()
    assert len(turmas) == 9


def test_existe_retorna_true_para_turma_cadastrada(app):
    assert repo.existe(1) is True
    assert repo.existe(50) is False


def test_adicionar_turmas_nao_duplica_se_ja_existirem(app):
    repo.adicionar_turmas()
    assert Turma.query.count() == 9
