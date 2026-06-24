from src.models.turma import Turma

class TurmaRepository:
    def get_semana_atual(self, turma_id):
        print(f'get semana atual {turma_id}')
        turma = Turma.query.filter_by(turma=turma_id).first()
        print(f'get semana atual 2 {turma.semana_atual}')
        return turma.semana_atual