from src.repositories.aluno_repository import AlunoRepository
from src.repositories.turma_repository import TurmaRepository

aluno_repository = AlunoRepository()
turma_repository = TurmaRepository()

def adicionar_turmas():
    turma_repository.adicionar_turmas()

def get_alunos_turma(turma):
    return aluno_repository.get_alunos_turma(turma)
