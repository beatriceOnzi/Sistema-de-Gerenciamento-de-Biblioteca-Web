from src.repositories.aluno_repository import AlunoRepository
from src.repositories.turma_repository import TurmaRepository
from src.repositories.turmas_repository import TurmasRepository


aluno_repository = AlunoRepository()
turma_repository = TurmaRepository()
turmas_repository = TurmasRepository()

def get_alunos():
    return aluno_repository.get_alunos()

def get_aluno_by_nome(nome):
    return aluno_repository.get_aluno_by_nome(nome)

def criar_aluno(dados):
    return aluno_repository.criar_aluno(dados['nome'], dados['turma'])

def deletar_aluno(id):
    return aluno_repository.deletar_aluno(id)

def validar_aluno(dados):
    erros = []

    if len(dados.get('nome')) >= 100:
        erros.append("Digite um nome com menos de 100 caracteres")
    
    if len(dados.get('nome')) < 5:
        erros.append("Digite o nome completo do aluno")
    
    apenas_letras = dados.get('nome').replace(" ", "").isalpha()
    if not apenas_letras:
        erros.append("Digite apenas letras")
    
    turma_existe = turmas_repository.existe(dados.get('turma'))
    if not turma_existe:
        erros.append("Turma inválida")

    if aluno_repository.existe_by_name_turma(dados.get('nome'), dados.get('turma')):
        erros.append("Este aluno já está cadastrado")
    
    return erros

def existe_aluno(id):
    return aluno_repository.existe_aluno(id)