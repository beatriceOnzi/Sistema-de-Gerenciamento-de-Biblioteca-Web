from src.repositories.turma_repository import TurmaRepository

repo = TurmaRepository()


def test_get_semana_atual_comeca_em_1(app):
    assert repo.get_semana_atual(1) == 1


def test_avancar_semana_incrementa_em_1(app):
    repo.avancar_semana(1)
    assert repo.get_semana_atual(1) == 2


def test_avancar_semana_retorna_a_turma_atualizada(app):
    turma = repo.avancar_semana(2)
    assert turma.semana_atual == 2
