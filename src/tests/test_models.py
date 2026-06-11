from src.models import db
from src.models.turma import Turma


def test_criar_turma(app):
    nova_turma = Turma(turma=10, turma_formatada = "10º Ano")
    db.session.add(nova_turma)
    db.session.commit()

    resultado = Turma.query.filter_by(turma=10).first()

    assert resultado.turma == 10