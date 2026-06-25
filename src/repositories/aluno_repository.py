from src.models import db, Aluno

class AlunoRepository:
    def get_alunos(self):
        alunos = Aluno.query.order_by(Aluno.turma).all()
        return alunos

    def get_aluno_by_nome(self, nome):
        aluno = Aluno.query.filter_by(nome=nome).first()
        return aluno

    def criar_aluno(self, nome_aluno, turma):
        novo_aluno = Aluno(nome=nome_aluno, turma=turma)
        db.session.add(novo_aluno)
        db.session.commit()

    def deletar_aluno(self, id):
        aluno = db.session.get(Aluno, id)
        if aluno:
            db.session.delete(aluno)
            db.session.commit()
        
    def get_alunos_turma(self, turma_id):
        alunos_turma = Aluno.query.filter_by(turma=turma_id).order_by(Aluno.nome).all()
        return alunos_turma
    
    def existe_aluno(self, id):
        return Aluno.query.filter_by(id=id).first() is not None
