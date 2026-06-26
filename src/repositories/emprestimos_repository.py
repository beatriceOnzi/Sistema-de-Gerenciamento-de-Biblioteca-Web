from src.models import db, Emprestimo, Aluno
from datetime import date

class EmprestimosRepository:
    def get_emprestimos_record(self, turma, semana_atual):
        turma = int(turma)
        semana_record = semana_atual - 1
        emprestimos = Emprestimo.query.join(Aluno).filter(
            Emprestimo.turma == turma,
            Emprestimo.semana == semana_record
        ).order_by(Aluno.nome).all()
        return [self.serialize_emprestimo(emp) for emp in emprestimos]
    
    def get_emprestimos_cadastro(self, turma, semana_atual):
        turma = int(turma)
        emprestimos = Emprestimo.query.join(Aluno).filter(
            Emprestimo.turma == turma,
            Emprestimo.semana == semana_atual
        ).order_by(Aluno.nome).all()
        return [self.serialize_emprestimo(emp) for emp in emprestimos]
    
    def get_emprestimo_record(self, aluno, turma, semana_record):
        turma = int(turma)
        emprestimo = Emprestimo.query.join(Aluno).filter(
            Aluno.nome == aluno,
            Emprestimo.turma == turma,
            Emprestimo.semana == semana_record
        ).order_by(Aluno.nome).first()
        print(emprestimo)
        return emprestimo
    
    def save_title(self, id, livro_id):
        emprestimo = Emprestimo.query.filter_by(id = id).one()
        emprestimo.livro_id = livro_id
        db.session.commit()
    
    def limpar_livro_emprestimo(self, id):
        emprestimo = Emprestimo.query.filter_by(id = id).one()
        emprestimo.livro_id = None
        db.session.commit()
    
    def set_data_devolucao(self, emprestimo):
        emprestimo.data_devolucao = date.today()
        db.session.commit()

    def limpar_data_devolucao(self, emprestimo):
        emprestimo.data_devolucao = None
        db.session.commit()

    def criar_semana_emprestimos(self, turma, alunos, semana):
        for aluno in alunos:
            novo_emprestimo = Emprestimo(
                aluno_id=aluno.id,
                turma=turma,
                semana=semana
            )
            db.session.add(novo_emprestimo)
        db.session.commit()
        return "implementar"

    def serialize_emprestimo(self, emp):
        return {
            "id": emp.id,
            "aluno": emp.aluno.nome if emp.aluno else None,
            "livro": emp.livro.nome if emp.livro else None,
            "data_emprestimo": emp.data_emprestimo.isoformat() if emp.data_emprestimo else None,
            "data_devolucao_prevista": emp.data_devolucao_prevista.isoformat() if emp.data_devolucao_prevista else None,
            "data_devolucao": emp.data_devolucao.isoformat() if emp.data_devolucao else None
        }