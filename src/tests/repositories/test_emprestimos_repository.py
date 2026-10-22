from src.repositories.aluno_repository import AlunoRepository
from src.repositories.emprestimos_repository import EmprestimosRepository
from src.models.emprestimo import Emprestimo

aluno_repository = AlunoRepository()
repo = EmprestimosRepository()


def _criar_aluno(nome, turma):
    aluno_repository.criar_aluno(nome, turma)
    return aluno_repository.get_aluno_by_nome(nome)


def test_criar_semana_emprestimos_cria_um_registro_por_aluno(app):
    aluno1 = _criar_aluno("Aluno Repo Um", 3)
    aluno2 = _criar_aluno("Aluno Repo Dois", 3)

    repo.criar_semana_emprestimos(3, [aluno1, aluno2], 1)

    emprestimos = Emprestimo.query.filter_by(turma=3).all()
    assert len(emprestimos) == 2


def test_get_emprestimos_cadastro_filtra_por_turma_e_semana(app):
    aluno = _criar_aluno("Aluno Repo Tres", 4)
    repo.criar_semana_emprestimos(4, [aluno], 1)

    cadastro = repo.get_emprestimos_cadastro(4, 1)

    assert len(cadastro) == 1
    assert cadastro[0].aluno.nome == "Aluno Repo Tres"


def test_get_emprestimos_cadastro_ignora_outras_semanas(app):
    aluno = _criar_aluno("Aluno Repo Semana", 4)
    repo.criar_semana_emprestimos(4, [aluno], 1)

    assert repo.get_emprestimos_cadastro(4, 2) == []


def test_get_emprestimos_record_filtra_pela_semana_anterior(app):
    aluno = _criar_aluno("Aluno Repo Quatro", 5)
    repo.criar_semana_emprestimos(5, [aluno], 1)

    record = repo.get_emprestimos_record(5, 2)

    assert len(record) == 1
    assert record[0].aluno.nome == "Aluno Repo Quatro"


def test_get_emprestimo_record_encontra_pelo_aluno_turma_e_semana(app):
    aluno = _criar_aluno("Aluno Repo Cinco", 6)
    repo.criar_semana_emprestimos(6, [aluno], 1)

    emprestimo = repo.get_emprestimo_record("Aluno Repo Cinco", 6, 1)

    assert emprestimo is not None
    assert emprestimo.aluno.nome == "Aluno Repo Cinco"


def test_get_emprestimo_record_retorna_none_se_nao_existir(app):
    assert repo.get_emprestimo_record("Ninguém", 6, 1) is None


def test_get_emprestimo_retorna_pelo_id(app):
    aluno = _criar_aluno("Aluno Repo Busca Id", 2)
    repo.criar_semana_emprestimos(2, [aluno], 1)
    criado = Emprestimo.query.filter_by(turma=2).first()

    emprestimo = repo.get_emprestimo(criado.id)

    assert emprestimo.id == criado.id
    assert emprestimo.aluno.nome == "Aluno Repo Busca Id"


def test_save_title_associa_livro_ao_emprestimo(app):
    aluno = _criar_aluno("Aluno Repo Seis", 7)
    repo.criar_semana_emprestimos(7, [aluno], 1)
    emprestimo = Emprestimo.query.filter_by(turma=7).first()

    repo.save_title(emprestimo.id, 1, "Livro Teste")

    atualizado = Emprestimo.query.filter_by(id=emprestimo.id).first()
    assert atualizado.livro_id == 1
    assert atualizado.livro_nome == "Livro Teste"


def test_limpar_livro_emprestimo_remove_associacao(app):
    aluno = _criar_aluno("Aluno Repo Sete", 8)
    repo.criar_semana_emprestimos(8, [aluno], 1)
    emprestimo = Emprestimo.query.filter_by(turma=8).first()
    repo.save_title(emprestimo.id, 1, "Livro Teste")

    repo.limpar_livro_emprestimo(emprestimo.id)

    atualizado = Emprestimo.query.filter_by(id=emprestimo.id).first()
    assert atualizado.livro_id is None


def test_set_data_devolucao_preenche_a_data_e_retorna(app):
    aluno = _criar_aluno("Aluno Repo Oito", 9)
    repo.criar_semana_emprestimos(9, [aluno], 1)
    emprestimo = Emprestimo.query.filter_by(turma=9).first()

    data = repo.set_data_devolucao(emprestimo)

    assert emprestimo.data_devolucao is not None
    assert data == emprestimo.data_devolucao


def test_limpar_data_devolucao_remove_a_data(app):
    aluno = _criar_aluno("Aluno Repo Nove", 1)
    repo.criar_semana_emprestimos(1, [aluno], 1)
    emprestimo = Emprestimo.query.filter_by(turma=1).first()
    repo.set_data_devolucao(emprestimo)

    resultado = repo.limpar_data_devolucao(emprestimo)

    assert emprestimo.data_devolucao is None
    assert resultado is None


def test_get_historico_retorna_apenas_emprestimos_com_livro(app):
    aluno1 = _criar_aluno("Aluno Repo Hist Um", 3)
    aluno2 = _criar_aluno("Aluno Repo Hist Dois", 3)
    repo.criar_semana_emprestimos(3, [aluno1, aluno2], 1)
    com_livro = Emprestimo.query.filter_by(aluno_id=aluno1.id).first()
    repo.save_title(com_livro.id, 1, "Livro Histórico")

    historico = repo.get_historico()

    assert [e.id for e in historico] == [com_livro.id]
    assert historico[0].livro_nome == "Livro Histórico"


def test_get_historico_vazio_sem_livros(app):
    aluno = _criar_aluno("Aluno Repo Hist Tres", 3)
    repo.criar_semana_emprestimos(3, [aluno], 1)

    assert repo.get_historico() == []
