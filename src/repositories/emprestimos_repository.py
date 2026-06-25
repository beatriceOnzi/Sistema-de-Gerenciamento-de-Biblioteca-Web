from src.models import db, Emprestimo

class EmprestimosRepository:
    def get_emprestimos_record(self, turma, semana_atual):
        turma = int(turma)
        semana_record = semana_atual - 1
        emprestimos = Emprestimo.query.filter(
            Emprestimo.turma == turma,
            Emprestimo.semana == semana_record
        ).all()
        return [self.serialize_emprestimo(emp) for emp in emprestimos]
    
    def get_emprestimos_cadastro(self, turma, semana_atual):
        turma = int(turma)
        semana_record = semana_atual
        emprestimos = Emprestimo.query.filter(
            Emprestimo.turma == turma,
            Emprestimo.semana == semana_record
        ).all()
        return [self.serialize_emprestimo(emp) for emp in emprestimos]

    def serialize_emprestimo(self, emp):
        return {
            "id": emp.id,
            "aluno": emp.aluno.nome if emp.aluno else None,
            "livro": emp.livro.nome if emp.livro else None,
            "data_emprestimo": emp.data_emprestimo.isoformat() if emp.data_emprestimo else None,
            "data_devolucao_prevista": emp.data_devolucao_prevista.isoformat() if emp.data_devolucao_prevista else None,
            "data_devolucao": emp.data_devolucao.isoformat() if emp.data_devolucao else None
        }