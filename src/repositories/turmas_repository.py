from src.models import db, Turma

class TurmasRepository:
    def get_turmas(self):
        return Turma.query.all()
        
    def existe(self, turma_id):
        return Turma.query.filter_by(turma=turma_id).first() is not None
    
    def adicionar_turmas(self):
        if Turma.query.first():
            return

        for i in range(1, 10):

            turma = Turma(
                turma=i,
                turma_formatada=f"{i}º Ano"
            )

            db.session.add(turma)

        db.session.commit()
    