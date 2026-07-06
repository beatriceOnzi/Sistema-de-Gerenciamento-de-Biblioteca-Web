from src.services.aluno_service import criar_aluno
from src.services import emprestimos_service
from src.services import historico_service
from src.models.historico import Historico


def test_salvar_emprestimos_nao_lanca_excecao(app):
    criar_aluno({'nome': "Aluno Historico", 'turma': 3})
    emprestimos_service.criar_semana_emprestimos(3)
    emprestimos_service.avancar_semana(3)

    historico_service.salvar_emprestimos(3)


def test_salvar_emprestimos_ainda_nao_persiste_registros(app):
    criar_aluno({'nome': "Aluno Historico Dois", 'turma': 4})
    emprestimos_service.criar_semana_emprestimos(4)
    emprestimos_service.avancar_semana(4)

    historico_service.salvar_emprestimos(4)

    registros = Historico.query.all()
    assert registros == []
