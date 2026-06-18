from src.models.turma import Turma

class TurmaRepository:
    def get_turmas(self):
        return Turma.query.all()