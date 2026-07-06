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