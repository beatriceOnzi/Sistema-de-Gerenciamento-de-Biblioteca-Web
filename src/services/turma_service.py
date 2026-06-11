from src.models import db, Aluno, Turma

def adicionar_turmas():

    if Turma.query.first():
        return

    for i in range(1, 10):

        turma = Turma(
            turma=i,
            turma_formatada=f"{i}º Ano"
        )

        db.session.add(turma)

    db.session.commit()

def get_alunos_turma(turma):
    alunos_turma = Aluno.query.filter_by(turma=turma).all()
    return alunos_turma
