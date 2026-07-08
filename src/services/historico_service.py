from src.repositories.emprestimos_repository import EmprestimosRepository
from src.repositories.historico_repository import HistoricoRepository
from src.repositories.turma_repository import TurmaRepository

emprestimos_repository = EmprestimosRepository()
historico_repository = HistoricoRepository()
turma_repository = TurmaRepository()

def salvar_emprestimos(turma):
    semana_record = turma_repository.get_semana_atual(turma)
    emprestimos_semana = get_emprestimos_semana_concluida(turma, semana_record)
    historico_repository.salvar_emprestimos(emprestimos_semana)

def get_emprestimos_semana_concluida(turma, semana_record):
    emprestimos = emprestimos_repository.get_emprestimos_record(turma, semana_record - 1)
    return emprestimos

def get_historico():
    all_emprestimos = historico_repository.get_historico()
    return [serialize_historico(emp) for emp in all_emprestimos]

def set_data_devolucao(id):
    emprestimo = historico_repository.get_emprestimo_historico(id)

    if emprestimo.data_devolucao:
        data_devolucao = historico_repository.limpar_data_devolucao(emprestimo)

    else:
        data_devolucao = formatar_data(emprestimos_repository.set_data_devolucao(emprestimo))

    return data_devolucao

def serialize_historico(emp):
    return {
        "id": emp.id,
        "aluno": emp.nome if emp.nome else None,
        "livro": emp.livro if emp.livro else None,
        "data_emprestimo": formatar_data(emp.data_emprestimo),
        "data_devolucao": formatar_data(emp.data_devolucao),
        "turma": emp.turma if emp.turma else None
    }

def formatar_data(data):
    if data is None:
        return None

    return data.strftime("%d-%m-%Y")
