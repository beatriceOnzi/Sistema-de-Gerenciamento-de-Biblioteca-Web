from src.repositories.aluno_repository import AlunoRepository

repo = AlunoRepository()


def _criar(nome, turma):
    repo.criar_aluno(nome, turma)
    return repo.get_aluno_by_nome(nome)


def test_criar_aluno(app):
    repo.criar_aluno("Aluno Repo", 3)

    aluno = repo.get_aluno_by_nome("Aluno Repo")

    assert aluno is not None
    assert aluno.turma == 3


def test_existe_aluno(app):
    aluno = _criar("Aluno Existe", 1)

    assert repo.existe_aluno(aluno.id) is True
    assert repo.existe_aluno(9999) is False


def test_get_aluno_by_nome_encontra_aluno_existente(app):
    repo.criar_aluno("Aluno Busca", 2)

    aluno = repo.get_aluno_by_nome("Aluno Busca")

    assert aluno is not None
    assert aluno.turma == 2


def test_get_aluno_by_nome_retorna_none_se_nao_existir(app):
    assert repo.get_aluno_by_nome("Não Existe") is None


def test_get_alunos_ordena_por_turma_e_nome(app):
    repo.criar_aluno("Bruno Turma 5", 5)
    repo.criar_aluno("Ana Turma 5", 5)
    repo.criar_aluno("Aluno Turma 1", 1)

    alunos = repo.get_alunos()

    assert [(a.turma, a.nome) for a in alunos] == [
        (1, "Aluno Turma 1"),
        (5, "Ana Turma 5"),
        (5, "Bruno Turma 5"),
    ]


def test_deletar_aluno(app):
    aluno = _criar("Aluno Deletar", 2)

    repo.deletar_aluno(aluno.id)

    assert repo.get_aluno_by_nome("Aluno Deletar") is None


def test_deletar_aluno_inexistente_nao_levanta_erro(app):
    repo.deletar_aluno(9999)


def test_desativar_aluno(app):
    aluno = _criar("Aluno Desativar", 2)

    repo.desativar_aluno(aluno.id)

    assert repo.status_aluno(aluno.id) is False


def test_ativar_aluno(app):
    aluno = _criar("Aluno Ativar", 2)
    repo.desativar_aluno(aluno.id)

    repo.ativar_aluno(aluno.id)

    assert repo.status_aluno(aluno.id) is True


def test_status_aluno_novo_e_ativo(app):
    aluno = _criar("Aluno Status", 2)

    assert repo.status_aluno(aluno.id) is True


def test_get_alunos_turma_corretamente(app):
    repo.criar_aluno("Aluno Turma 4 B", 4)
    repo.criar_aluno("Aluno Turma 4 A", 4)
    repo.criar_aluno("Aluno Turma 6", 6)

    alunos_turma_4 = repo.get_alunos_turma(4)

    assert [a.nome for a in alunos_turma_4] == ["Aluno Turma 4 A", "Aluno Turma 4 B"]
    assert all(a.turma == 4 for a in alunos_turma_4)


def test_get_alunos_ativos_turma_ignora_desativados(app):
    ativo = _criar("Aluno Ativo", 4)
    inativo = _criar("Aluno Inativo", 4)
    _criar("Aluno Outra Turma", 5)
    repo.desativar_aluno(inativo.id)

    alunos = repo.get_alunos_ativos_turma(4)

    assert [a.id for a in alunos] == [ativo.id]


def test_existe_by_name_turma(app):
    repo.criar_aluno("Aluno Duplicado", 2)

    assert repo.existe_by_name_turma("Aluno Duplicado", 2) is True
    assert repo.existe_by_name_turma("Aluno Duplicado", 3) is False
    assert repo.existe_by_name_turma("Outro Aluno", 2) is False


def test_avancar_ano(app):
    repo.criar_aluno("Aluno 1", 1)
    repo.criar_aluno("Aluno 2", 2)

    repo.avancar_turmas()

    assert repo.get_aluno_by_nome("Aluno 1").turma == 2
    assert repo.get_aluno_by_nome("Aluno 2").turma == 3


def test_avancar_ano_desativa_alunos_da_turma_9(app):
    formando = _criar("Aluno Formando", 9)
    outro = _criar("Aluno Oitavo", 8)

    repo.avancar_turmas()

    assert repo.status_aluno(formando.id) is False
    assert repo.get_aluno_by_nome("Aluno Formando").turma == 9
    assert repo.status_aluno(outro.id) is True
    assert repo.get_aluno_by_nome("Aluno Oitavo").turma == 9
