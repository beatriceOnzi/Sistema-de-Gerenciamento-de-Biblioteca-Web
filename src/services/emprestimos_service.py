from src.repositories.aluno_repository import AlunoRepository
from src.repositories.livro_repository import LivroRepository
from src.repositories.turma_repository import TurmaRepository
from src.repositories.turmas_repository import TurmasRepository
from src.repositories.emprestimos_repository import EmprestimosRepository

aluno_repository = AlunoRepository()
livro_repository= LivroRepository()
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

def save_title(id, titulo):
    if titulo == "" or titulo == None:
        limpar_livro_emprestimo(id)
        return
    livro_id = livro_repository.get_id_by_title(titulo)
    emprestimos_repository.save_title(id, livro_id)

def set_data_devolucao(titulo, aluno, turma):
    semana_record = get_semana_atual(turma) - 1

    emprestimo_record = emprestimos_repository.get_emprestimo_record(aluno, turma, semana_record)
    
    if titulo == "" or titulo == None:
        emprestimos_repository.limpar_data_devolucao(emprestimo_record)
    else:
        emprestimos_repository.set_data_devolucao(emprestimo_record)
    
def limpar_livro_emprestimo(id):
    emprestimos_repository.limpar_livro_emprestimo(id)

def criar_semana_emprestimos(turma):
    avancar_semana(turma)
    nova_semana = emprestimos_repository.criar_semana_emprestimos(turma, get_alunos_turma(turma), get_semana_atual(turma))
    return nova_semana