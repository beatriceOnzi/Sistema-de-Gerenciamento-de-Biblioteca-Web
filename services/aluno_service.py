from models import db, Aluno

def get_alunos():
    alunos = Aluno.query.order_by(Aluno.turma).all()
    return alunos

def novoAluno(nome_aluno, turma):
    novo_aluno = Aluno(nome=nome_aluno, turma=turma)
    db.session.add(novo_aluno)
    db.session.commit()

def deleteAluno(id):
    aluno = db.session.get(Aluno, id)
    if aluno:
        db.session.delete(aluno)
        db.session.commit()