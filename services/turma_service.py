from models import db, Aluno

def get_alunos_turma(turma):
    alunos_turma = Aluno.query.filter_by(turma=turma).all()
    return alunos_turma
