from src.models import db
from src.models.turma import Turma
from src.models.aluno import Aluno
from src.models.livro import Livro
from src.models.emprestimo import Emprestimo
from datetime import date, timedelta


def test_criar_turma(app):
    nova_turma = Turma(turma=10, turma_formatada = "10º Ano")
    db.session.add(nova_turma)
    db.session.commit()

    resultado = Turma.query.filter_by(turma=10).first()

    assert resultado.turma == 10


def test_criar_aluno(app):
    aluno = Aluno(nome="Aluno Model", turma=1)
    db.session.add(aluno)
    db.session.commit()

    resultado = Aluno.query.filter_by(nome="Aluno Model").first()

    assert resultado.turma == 1


def test_criar_livro(app):
    livro = Livro(nome="Livro Model")
    db.session.add(livro)
    db.session.commit()

    resultado = Livro.query.filter_by(nome="Livro Model").first()

    assert resultado.nome == "Livro Model"


def test_emprestimo_data_devolucao_prevista_padrao_e_sete_dias(app):
    aluno = Aluno(nome="Aluno Prazo", turma=1)
    db.session.add(aluno)
    db.session.commit()

    emprestimo = Emprestimo(aluno_id=aluno.id, turma=1, semana=1)
    db.session.add(emprestimo)
    db.session.commit()

    assert emprestimo.data_devolucao_prevista == date.today() + timedelta(days=7)


def test_emprestimo_relacionamento_com_aluno(app):
    aluno = Aluno(nome="Aluno Relacao", turma=1)
    db.session.add(aluno)
    db.session.commit()

    emprestimo = Emprestimo(aluno_id=aluno.id, turma=1, semana=1)
    db.session.add(emprestimo)
    db.session.commit()

    assert emprestimo.aluno.nome == "Aluno Relacao"
    assert aluno.emprestimos[0].id == emprestimo.id