from src.models import db, Historico
from datetime import datetime

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
                    turma = emprestimo.turma
                )
                print(novo_registro)
                db.session.add(novo_registro)
        db.session.commit()