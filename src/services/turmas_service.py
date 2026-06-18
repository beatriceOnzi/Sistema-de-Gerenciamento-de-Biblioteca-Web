from src.repositories.turmas_repository import TurmaRepository

turma_repository = TurmaRepository()

def get_turmas():
    turmas = turma_repository.get_turmas()
    return turmas