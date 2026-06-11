from src.models import db, Emprestimo
from datetime import date, timedelta

# exemplo feito de metodos ilegais - ignorar
def criar_emprestimo(aluno_id, livro_id):

    data_devolucao = date.today() + timedelta(days=7)

    emprestimo = Emprestimo(
        aluno_id=aluno_id,
        livro_id=livro_id,
        data_devolucao_prevista=data_devolucao
    )

    db.session.add(emprestimo)
    db.session.commit()

    return emprestimo