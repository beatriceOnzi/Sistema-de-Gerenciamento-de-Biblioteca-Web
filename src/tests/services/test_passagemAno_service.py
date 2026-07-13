import src.services.passagemAno_service as service
from src.repositories.aluno_repository import AlunoRepository

repo = AlunoRepository()

def test_avancar_ano(app):
    repo.criar_aluno("Aluno 1", 1)
    repo.criar_aluno("Aluno 2", 2)

    service.avancar_turmas()

    aluno1 = repo.get_aluno_by_nome("Aluno 1")
    aluno2 = repo.get_aluno_by_nome("Aluno 2")

    assert aluno1.turma == 2
    assert aluno2.turma == 3