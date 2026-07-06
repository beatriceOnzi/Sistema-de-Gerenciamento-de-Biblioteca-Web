from src.repositories.historico_repository import HistoricoRepository
from src.models.historico import Historico

repo = HistoricoRepository()


def test_salvar_emprestimos_nao_lanca_excecao(app):
    repo.salvar_emprestimos([])


def test_salvar_emprestimos_retorna_string_fixa(app):
    resultado = repo.salvar_emprestimos([])
    assert resultado == "teste"


def test_salvar_emprestimos_ainda_nao_persiste_no_banco(app):
    repo.salvar_emprestimos([{"aluno": "Teste"}])

    assert Historico.query.all() == []
