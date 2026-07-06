from src.services.aluno_service import criar_aluno
from src.services import emprestimos_service
from src.models.emprestimo import Emprestimo
from src.models.livro import Livro


def test_get_semana_atual_comeca_na_semana_1(app):
    semana = emprestimos_service.get_semana_atual(3)
    assert semana == 1


def test_avancar_semana_incrementa_semana_atual(app):
    emprestimos_service.avancar_semana(3)
    semana = emprestimos_service.get_semana_atual(3)
    assert semana == 2


def test_criar_semana_emprestimos_gera_um_emprestimo_por_aluno(app):
    criar_aluno({'nome': "Aluno Um", 'turma': 5})
    criar_aluno({'nome': "Aluno Dois", 'turma': 5})

    emprestimos_service.criar_semana_emprestimos(5)

    emprestimos = Emprestimo.query.filter_by(turma=5).all()
    assert len(emprestimos) == 2


def test_get_emprestimos_cadastro_lista_emprestimos_da_semana_atual(app):
    criar_aluno({'nome': "Aluno Tres", 'turma': 6})
    emprestimos_service.criar_semana_emprestimos(6)

    cadastro = emprestimos_service.get_emprestimos_cadastro(6)

    assert len(cadastro) == 1
    assert cadastro[0]['aluno'] == "Aluno Tres"
    assert cadastro[0]['livro'] is None


def test_get_emprestimos_record_lista_emprestimos_da_semana_anterior(app):
    criar_aluno({'nome': "Aluno Quatro", 'turma': 7})
    emprestimos_service.criar_semana_emprestimos(7)

    record = emprestimos_service.get_emprestimos_record(7)

    assert record == []


def test_save_title_cria_livro_automaticamente_se_nao_existir(app):
    criar_aluno({'nome': "Aluno Cinco", 'turma': 8})
    emprestimos_service.criar_semana_emprestimos(8)
    emprestimo = Emprestimo.query.filter_by(turma=8).first()

    emprestimos_service.save_title(emprestimo.id, "Livro Novo")

    livro = Livro.query.filter_by(nome="Livro Novo").first()
    cadastro = emprestimos_service.get_emprestimos_cadastro(8)
    assert livro is not None
    assert cadastro[0]['livro'] == "Livro Novo"


def test_save_title_com_titulo_vazio_limpa_o_livro(app):
    criar_aluno({'nome': "Aluno Seis", 'turma': 9})
    emprestimos_service.criar_semana_emprestimos(9)
    emprestimo = Emprestimo.query.filter_by(turma=9).first()
    emprestimos_service.save_title(emprestimo.id, "Outro Livro")

    emprestimos_service.save_title(emprestimo.id, "")

    cadastro = emprestimos_service.get_emprestimos_cadastro(9)
    assert cadastro[0]['livro'] is None


def test_set_data_devolucao_preenche_data_quando_titulo_informado(app):
    criar_aluno({'nome': "Aluno Sete", 'turma': 1})
    emprestimos_service.criar_semana_emprestimos(1)
    emprestimos_service.avancar_semana(1)

    data = emprestimos_service.set_data_devolucao("Algum Livro", "Aluno Sete", 1)

    assert data is not None


def test_set_data_devolucao_com_titulo_vazio_limpa_data(app):
    criar_aluno({'nome': "Aluno Oito", 'turma': 2})
    emprestimos_service.criar_semana_emprestimos(2)
    emprestimos_service.avancar_semana(2)

    data = emprestimos_service.set_data_devolucao("", "Aluno Oito", 2)

    assert data is None
