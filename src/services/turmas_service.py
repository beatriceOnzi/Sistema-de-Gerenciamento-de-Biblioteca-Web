from src.repositories.turmas_repository import TurmasRepository

turmas_repository = TurmasRepository()

def get_turmas():
    turmas = turmas_repository.get_turmas()
    if not turmas:
        turmas_repository.adicionar_turmas()
        turmas = turmas_repository.get_turmas()
    return turmas