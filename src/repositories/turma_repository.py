from src.models.turma import Turma

class TurmaRepository:
    def get_semana_atual(self, turma_id):
        turma = Turma.query.filter_by(turma=turma_id).first()
        return turma.semana_atual