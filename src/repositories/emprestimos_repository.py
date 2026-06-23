from src.models import db, Emprestimo

class EmprestimosRepository:
    def get_emprestimos_record(self, turma, semana_atual):
        semana_record = semana_atual - 1
        emprestimos = Emprestimo.query.filter_by(turma = turma, semana = semana_record ).all()
        return emprestimos