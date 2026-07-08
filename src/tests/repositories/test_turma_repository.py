from src.repositories.turma_repository import TurmaRepository
from src.models.turma import Turma

repo = TurmaRepository()


def test_get_semana_atual(app):
    assert repo.get_semana_atual(1) == 1


def test_avancar_semana_incrementa_em_1(app):
    repo.avancar_semana(3)
    assert Turma.query.filter_by(turma=3).first().semana_atual == 2
    repo.avancar_semana(3)
    assert Turma.query.filter_by(turma=3).first().semana_atual == 3

