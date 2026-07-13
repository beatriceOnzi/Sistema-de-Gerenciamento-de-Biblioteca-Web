from src.repositories.aluno_repository import AlunoRepository

aluno_repository = AlunoRepository()

def avancar_turmas():
    mensagem = aluno_repository.avancar_turmas()
    return mensagem