import src.services.turmas_service as service
from src.repositories.turmas_repository import TurmasRepository

repo = TurmasRepository()

def test_adicionar_turmas(app):
    service.adicionar_turmas()
    turmas = repo.get_turmas()
    assert len(turmas) == 9

def test_get_turmas(app):
    turmas = service.get_turmas()
    assert len(turmas) == 9