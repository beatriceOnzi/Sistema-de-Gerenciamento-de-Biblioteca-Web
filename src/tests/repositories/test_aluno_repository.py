from src.repositories.aluno_repository import AlunoRepository

repo = AlunoRepository()


def test_criar_aluno_persiste_no_banco(app):
    repo.criar_aluno("Aluno Repo", 3)

    aluno = repo.get_aluno_by_nome("Aluno Repo")

    assert aluno is not None
    assert aluno.turma == 3


def test_get_alunos_ordena_por_turma(app):
    repo.criar_aluno("Aluno Turma 5", 5)
    repo.criar_aluno("Aluno Turma 1", 1)

    alunos = repo.get_alunos()

    assert [a.turma for a in alunos] == sorted(a.turma for a in alunos)


def test_get_aluno_by_nome_encontra_aluno_existente(app):
    repo.criar_aluno("Aluno Busca", 2)

    aluno = repo.get_aluno_by_nome("Aluno Busca")

    assert aluno is not None
    assert aluno.turma == 2


def test_get_aluno_by_nome_retorna_none_se_nao_existir(app):
    aluno = repo.get_aluno_by_nome("Nao Existe")
    assert aluno is None


def test_deletar_aluno_remove_do_banco(app):
    repo.criar_aluno("Aluno Deletar", 2)
    aluno = repo.get_aluno_by_nome("Aluno Deletar")

    repo.deletar_aluno(aluno.id)

    assert repo.get_aluno_by_nome("Aluno Deletar") is None


def test_deletar_aluno_inexistente_nao_lanca_excecao(app):
    repo.deletar_aluno(9999)


def test_get_alunos_turma_filtra_pela_turma_correta(app):
    repo.criar_aluno("Aluno Turma 4 A", 4)
    repo.criar_aluno("Aluno Turma 4 B", 4)
    repo.criar_aluno("Aluno Turma 6", 6)

    alunos_turma_4 = repo.get_alunos_turma(4)

    assert len(alunos_turma_4) == 2
    assert all(a.turma == 4 for a in alunos_turma_4)


def test_existe_aluno(app):
    repo.criar_aluno("Aluno Existe", 1)
    aluno = repo.get_aluno_by_nome("Aluno Existe")

    assert repo.existe_aluno(aluno.id) is True
    assert repo.existe_aluno(9999) is False


def test_existe_by_name_turma(app):
    repo.criar_aluno("Aluno Duplicado", 2)

    assert repo.existe_by_name_turma("Aluno Duplicado", 2) is True
    assert repo.existe_by_name_turma("Aluno Duplicado", 3) is False
