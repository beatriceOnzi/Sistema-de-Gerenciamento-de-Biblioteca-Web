from src.models import db, Turma

def get_turmas():
    turmas = Turma.query.all()
    return turmas