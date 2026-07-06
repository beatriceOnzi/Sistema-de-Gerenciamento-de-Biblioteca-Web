from src.repositories.livro_repository import LivroRepository
from src.models.livro import Livro

repo = LivroRepository()


def test_criar_livro_persiste_no_banco(app):
    repo.criar_livro("Livro Repo")

    livro = Livro.query.filter_by(nome="Livro Repo").first()
    assert livro is not None


def test_criar_livro_remove_espacos_extras(app):
    repo.criar_livro("  Livro Com Espacos  ")

    livro = Livro.query.filter_by(nome="Livro Com Espacos").first()
    assert livro is not None


def test_get_livros_ordena_por_nome(app):
    repo.criar_livro("Zebra")
    repo.criar_livro("Abelha")

    livros = repo.get_livros()

    assert [l.nome for l in livros] == ["Abelha", "Zebra"]


def test_existe_retorna_true_para_livro_cadastrado(app):
    repo.criar_livro("Livro Existente")

    assert repo.existe("Livro Existente") is True
    assert repo.existe("Livro Inexistente") is False


def test_deletar_livro_remove_do_banco(app):
    repo.criar_livro("Livro Deletar")
    livro = Livro.query.filter_by(nome="Livro Deletar").first()

    repo.deletar_livro(livro.id)

    assert Livro.query.filter_by(nome="Livro Deletar").first() is None


def test_deletar_livro_inexistente_nao_lanca_excecao(app):
    repo.deletar_livro(9999)


def test_get_id_by_title_retorna_id_existente(app):
    repo.criar_livro("Livro Id")
    livro = Livro.query.filter_by(nome="Livro Id").first()

    id_encontrado = repo.get_id_by_title("Livro Id")

    assert id_encontrado == livro.id


def test_get_id_by_title_cria_livro_se_nao_existir(app):
    id_criado = repo.get_id_by_title("Livro Criado Na Busca")

    livro = Livro.query.filter_by(nome="Livro Criado Na Busca").first()
    assert livro is not None
    assert id_criado == livro.id
