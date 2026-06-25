from src.models.turma import db, Turma

class TurmaRepository:
    def get_semana_atual(self, turma_id):
        turma = Turma.query.filter_by(turma=turma_id).first()
        return turma.semana_atual
    
    def avancar_semana(self, turma_id):
        turma = Turma.query.filter_by(turma=turma_id).first()
        turma.semana_atual = turma.semana_atual + 1
        db.session.commit()
        return turma