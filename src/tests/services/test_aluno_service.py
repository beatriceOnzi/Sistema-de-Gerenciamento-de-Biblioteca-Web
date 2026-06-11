from src.services.aluno_service import criar_aluno, deletar_aluno, validar_aluno
from src.models.aluno import Aluno


def test_criar_criar_aluno(app):

    criar_aluno("Beatrice teste", 3)

    aluno_teste = Aluno.query.filter_by(
        nome="Beatrice teste"
    ).first()

    assert aluno_teste.nome == "Beatrice teste"
    assert aluno_teste.turma == 3

def test_deletar_aluno(app):
    criar_aluno("Beatrice teste", 3)
    aluno_teste = Aluno.query.filter_by(nome="Beatrice teste").first()

    assert aluno_teste is not None

    deletar_aluno(aluno_teste.id)
    aluno_deletado = Aluno.query.filter_by(nome="Beatrice teste").first()

    assert aluno_deletado is None

def test_validar_aluno_correto(app):
    erros = validar_aluno("Beatrice Nome Válido", 3)
    assert len(erros) == 0

def test_validar_aluno_muitos_caracteres(app):
    erros = validar_aluno("Essa String tem mais de 120 caracteres At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium", 4)
    assert "Digite um nome com menos de 120 caracteres" in erros

def test_validar_aluno_poucos_caracteres(app):
    erros = validar_aluno("A", 4)
    assert "Digite o nome completo do aluno" in erros

def test_validar_aluno_caracteres_proibidos(app):
    erros = validar_aluno("Esse nome possui algo alem de letras $", 4)
    assert "Digite apenas letras" in erros

def test_aluno_turma_invalida(app):
    erros = validar_aluno("Nome Exemplo", 10)
    assert "Turma inválida" in erros