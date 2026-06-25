from src.repositories.aluno_repository import AlunoRepository
from src.repositories.turma_repository import TurmaRepository
from src.repositories.turmas_repository import TurmasRepository
from src.repositories.emprestimos_repository import EmprestimosRepository

aluno_repository = AlunoRepository()
turma_repository = TurmaRepository()
turmas_repository = TurmasRepository()
emprestimos_repository = EmprestimosRepository()

def get_alunos_turma(turma):
    return aluno_repository.get_alunos_turma(turma)

def get_semana_atual(turma):
    return turma_repository.get_semana_atual(turma)

def avancar_semana(turma):
    turma = turma_repository.avancar_semana(turma)

def get_emprestimos_record(turma):
    semana_atual = get_semana_atual(turma)
    emprestimos = emprestimos_repository.get_emprestimos_record(turma, semana_atual)
    return emprestimos

def get_emprestimos_cadastro(turma):
    semana_atual = get_semana_atual(turma)
    emprestimos = emprestimos_repository.get_emprestimos_cadastro(turma, semana_atual)
    return emprestimos
    #tenta pegar os emprestimos da semana atual (model turma) para exibir data (hj)/nome/________/datadevolcao prevista
    # se nao existir, cria

def create_emprestimos_cadastro(turma):
    # chamado quando clica em avancar semana
    # cria emprestimos no banco para cada aluno com os dados:
    # hoje / nome / ________/ data devolucao prevista
    return "implementar"