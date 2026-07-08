import src.services.aluno_service as aluno_service
import src.services.livro_service as livro_service
import src.services.emprestimos_service as service
from src.repositories.emprestimos_repository import EmprestimosRepository

repo = EmprestimosRepository()

def test_get_semana_atual_comeca_na_semana_1(app):
    semana = service.get_semana_atual(3)
    assert semana == 1


def test_avancar_semana_incrementa_semana_atual(app):
    service.avancar_semana(3)
    semana = service.get_semana_atual(3)
    assert semana == 2


def test_criar_semana_gera_um_emprestimo_por_aluno(app):
    aluno_service.criar_aluno({'nome': "Aluno Um", 'turma': 5})
    aluno_service.criar_aluno({'nome': "Aluno Dois", 'turma': 5})

    service.criar_semana_emprestimos(5)

    emprestimos = repo.get_emprestimos_cadastro(5, 1)
    assert len(emprestimos) == 2


def test_get_emprestimos_cadastro_lista_emprestimos_da_semana_atual(app):
    aluno_service.criar_aluno({'nome': "Aluno Tres", 'turma': 6})
    service.criar_semana_emprestimos(6)

    cadastro = service.get_emprestimos_cadastro(6)

    assert len(cadastro) == 1
    assert cadastro[0]['aluno'] == "Aluno Tres"
    assert cadastro[0]['livro'] is None


def test_get_emprestimos_record_lista_emprestimos_da_semana_anterior(app):
    aluno_service.criar_aluno({'nome': "Aluno Quatro", 'turma': 7})
    service.criar_semana_emprestimos(7)

    record = service.get_emprestimos_record(7)

    assert record == []


def test_save_title_cria_livro_automaticamente_se_nao_existir(app):
    aluno_service.criar_aluno({'nome': "Aluno Cinco", 'turma': 8})
    service.criar_semana_emprestimos(8)
    emprestimo = repo.get_emprestimo_record("Aluno Cinco", 8, 1)

    service.save_title(emprestimo.id, "Livro Novo")

    livro = livro_service.get_livro_by_title("Livro Novo")

    emprestimos = repo.get_emprestimos_cadastro(8, 1)

    assert livro is not None
    assert emprestimos[0].livro.nome == "Livro Novo"


def test_save_title_com_titulo_vazio_limpa_o_livro(app):
    aluno_service.criar_aluno({'nome': "Aluno Seis", 'turma': 9})
    service.criar_semana_emprestimos(9)
    emprestimo = repo.get_emprestimo_record("Aluno Seis", 9, 1)
    service.save_title(emprestimo.id, "Outro Livro")

    service.save_title(emprestimo.id, "")

    emprestimos = repo.get_emprestimos_cadastro(9, 1)
    assert emprestimos[0].livro is None


def test_set_data_devolucao_preenche_data_quando_titulo_informado(app):
    aluno_service.criar_aluno({'nome': "Aluno Sete", 'turma': 1})
    service.criar_semana_emprestimos(1)
    service.avancar_semana(1)

    data = service.set_data_devolucao("Algum Livro", "Aluno Sete", 1)

    assert data is not None


def test_set_data_devolucao_com_titulo_vazio_limpa_data(app):
    aluno_service.criar_aluno({'nome': "Aluno Oito", 'turma': 2})
    service.criar_semana_emprestimos(2)
    service.avancar_semana(2)

    data = service.set_data_devolucao("", "Aluno Oito", 2)

    assert data is None
