from src.models import db, Historico
from datetime import date

class HistoricoRepository:
    def salvar_emprestimos(self, emprestimos):
        for emprestimo in emprestimos:
            if emprestimo.livro != None:
                novo_registro = Historico(
                    id_emprestimo = emprestimo.id,
                    nome = emprestimo.aluno.nome,
                    livro = emprestimo.livro.nome,
                    data_emprestimo = emprestimo.data_emprestimo,
                    data_devolucao = emprestimo.data_devolucao,
                    turma = self.formatar_turma(emprestimo.turma)
                )
                print(novo_registro)
                db.session.add(novo_registro)
        db.session.commit()

    def get_historico(self):
        all_emprestimos = Historico.query.all()
        return all_emprestimos
    
    def set_data_devolucao(self, emprestimo):
        emprestimo.data_devolucao = date.today()
        db.session.commit()

        return emprestimo.data_devolucao

    def limpar_data_devolucao(self, emprestimo):
        emprestimo.data_devolucao = None
        db.session.commit()
        
        return None
    
    def formatar_turma(self, turma_int):
        turma_formatada=f"{turma_int}º Ano"
        return turma_formatada
    
    def get_emprestimo_historico(self, id):
        emprestimo = Historico.query.filter_by(id = id).one()
        return emprestimo