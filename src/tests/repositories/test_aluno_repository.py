from src.repositories.aluno_repository import AlunoRepository
from src.models.aluno import Aluno

repo = AlunoRepository()

def test_criar_aluno(app):
    repo.criar_aluno("Aluno Repo", 3)

    aluno = repo.get_aluno_by_nome("Aluno Repo")

    assert aluno is not None
    assert aluno.turma == 3

def test_existe_aluno(app):
    repo.criar_aluno("Aluno Existe", 1)
    aluno = Aluno.query.filter_by(nome="Aluno Existe").first()

    assert repo.existe_aluno(aluno.id) is True
    assert repo.existe_aluno(9999) is False

def test_get_aluno_by_nome_encontra_aluno_existente(app):
    repo.criar_aluno("Aluno Busca", 2)

    aluno = Aluno.query.filter_by(nome="Aluno Busca").first()

    assert aluno is not None
    assert aluno.turma == 2

def test_get_aluno_by_nome_retorna_none_se_nao_existir(app):
    aluno = Aluno.query.filter_by(nome="Não Existe").first()
    assert aluno is None

def test_get_alunos_ordena_por_turma(app):
    repo.criar_aluno("Aluno Turma 5", 5)
    repo.criar_aluno("Aluno Turma 1", 1)

    alunos = repo.get_alunos()

    assert [a.turma for a in alunos] == sorted(a.turma for a in alunos)

def test_deletar_aluno(app):
    repo.criar_aluno("Aluno Deletar", 2)
    aluno = Aluno.query.filter_by(nome="Aluno Deletar").first()

    repo.deletar_aluno(aluno.id)

    assert Aluno.query.filter_by(nome="Aluno Deletar").first() is None

def test_get_alunos_turma_corretamente(app):
    repo.criar_aluno("Aluno Turma 4 A", 4)
    repo.criar_aluno("Aluno Turma 4 B", 4)
    repo.criar_aluno("Aluno Turma 6", 6)

    alunos_turma_4 = repo.get_alunos_turma(4)

    assert len(alunos_turma_4) == 2
    assert all(a.turma == 4 for a in alunos_turma_4)

def test_existe_by_name_turma(app):
    repo.criar_aluno("Aluno Duplicado", 2)

    assert repo.existe_by_name_turma("Aluno Duplicado", 2) is True
    assert repo.existe_by_name_turma("Outro Aluno", 3) is False
