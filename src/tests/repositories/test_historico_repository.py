from datetime import date
from src.repositories.historico_repository import HistoricoRepository
from src.repositories.emprestimos_repository import EmprestimosRepository
from src.repositories.aluno_repository import AlunoRepository
from src.repositories.livro_repository import LivroRepository

from src.models.aluno import Aluno
from src.models.emprestimo import Emprestimo
from src.models.historico import Historico

historico_repo = HistoricoRepository()
emprestimo_repo = EmprestimosRepository()
aluno_repo = AlunoRepository()
livro_repo = LivroRepository()


def _criar_aluno(nome, turma):
    aluno_repo.criar_aluno(nome, turma)
    return aluno_repo.get_aluno_by_nome(nome)


def _criar_alunos_padrao(turma=3):
    aluno1 = _criar_aluno("Aluno Um", turma)
    aluno2 = _criar_aluno("Aluno Dois", turma)
    return [aluno1, aluno2]


def _criar_emprestimos_da_semana(turma, alunos, semana):
    emprestimo_repo.criar_semana_emprestimos(turma, alunos, semana)
    return emprestimo_repo.get_emprestimos_cadastro(turma, semana)


def _definir_livro_dos_emprestimos(emprestimos, livro_id):
    for emprestimo in emprestimos:
        emprestimo_repo.save_title(emprestimo.id, livro_id)


def _criar_historico_padrao(turma=3, semana=1, livro_titulo="Livro 1"):
    livro_repo.criar_livro(livro_titulo)
    alunos = _criar_alunos_padrao(turma=turma)

    emprestimos = _criar_emprestimos_da_semana(turma=turma, alunos=alunos, semana=semana)
    _definir_livro_dos_emprestimos(emprestimos, livro_id=1)

    historico_repo.salvar_emprestimos(emprestimos)
    return historico_repo.get_historico()


def test_retorna_lista_vazia_quando_nao_ha_historico(app):
    historico = historico_repo.get_historico()
    assert historico == []

def test_retorna_todos_os_emprestimos_salvos(app):
    historico = _criar_historico_padrao()
    assert len(historico) == 2

def test_retorna_historico_com_todas_as_semanas(app):
    _criar_historico_padrao(turma=3, semana=1)

    alunos_semana2 = _criar_alunos_padrao(turma=3)
    emprestimos_semana2 = _criar_emprestimos_da_semana(3, alunos_semana2, semana=2)

    _definir_livro_dos_emprestimos(emprestimos_semana2, livro_id=1)

    historico_repo.salvar_emprestimos(emprestimos_semana2)

    historico = historico_repo.get_historico()
    assert len(historico) == 4


def test_define_data_devolucao_como_hoje(app):
    historico = _criar_historico_padrao()
    emprestimo = historico[0]

    data_retornada = historico_repo.set_data_devolucao(emprestimo)

    assert data_retornada == date.today()
    assert emprestimo.data_devolucao == date.today()

def test_persiste_data_devolucao_no_banco(app):
    historico = _criar_historico_padrao()
    emprestimo = historico[0]

    historico_repo.set_data_devolucao(emprestimo)

    emprestimo_recarregado = Historico.query.filter_by(id = emprestimo.id).one()
    assert emprestimo_recarregado.data_devolucao == date.today()


def test_retorna_data_none(app):
    historico = _criar_historico_padrao()
    emprestimo = historico[0]
    historico_repo.set_data_devolucao(emprestimo)

    resultado = historico_repo.limpar_data_devolucao(emprestimo)

    assert resultado is None

def test_remove_data_devolucao_existente(app):
    historico = _criar_historico_padrao()
    emprestimo = historico[0]
    historico_repo.set_data_devolucao(emprestimo)
    assert emprestimo.data_devolucao == date.today()

    historico_repo.limpar_data_devolucao(emprestimo)

    assert emprestimo.data_devolucao is None

def test_persiste_remocao_no_banco(app):
    historico = _criar_historico_padrao()
    emprestimo = historico[0]
    historico_repo.set_data_devolucao(emprestimo)

    historico_repo.limpar_data_devolucao(emprestimo)

    emprestimo_recarregado = Historico.query.filter_by(id = emprestimo.id).one()
    assert emprestimo_recarregado.data_devolucao is None

def test_nao_gera_erro_quando_data_ja_e_none(app):
    historico = _criar_historico_padrao()
    emprestimo = historico[0]
    assert emprestimo.data_devolucao is None

    resultado = historico_repo.limpar_data_devolucao(emprestimo)

    assert resultado is None
    assert emprestimo.data_devolucao is None

def test_retorna_emprestimo_pelo_id(app):
    historico = _criar_historico_padrao()
    emprestimo_esperado = historico[0]

    emprestimo = historico_repo.get_emprestimo_historico(emprestimo_esperado.id)

    assert emprestimo.id == emprestimo_esperado.id