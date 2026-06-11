from src.models import db, Aluno, Turma

def get_alunos():
    alunos = Aluno.query.order_by(Aluno.turma).all()
    return alunos

def criar_aluno(nome_aluno, turma):
    novo_aluno = Aluno(nome=nome_aluno, turma=turma)
    db.session.add(novo_aluno)
    db.session.commit()

def deletar_aluno(id):
    aluno = db.session.get(Aluno, id)
    if aluno:
        db.session.delete(aluno)
        db.session.commit()

def validar_aluno(nome, turma):
    erros = []

    if len(nome) >= 120:
        erros.append("Digite um nome com menos de 120 caracteres")
    
    if len(nome) < 5:
        erros.append("Digite o nome completo do aluno")
    
    apenas_letras = nome.replace(" ", "").isalpha()
    if not apenas_letras:
        erros.append("Digite apenas letras")
    
    turma_existe = Turma.query.filter_by(turma=turma).first()
    if not turma_existe:
        erros.append("Turma inválida")
    
    return erros
    

# quando nao é validado, a pagina recarrega, e o nome/ turma que estava escrito, some. Tem como solucionar isso
# utilizando javascript, ou só passando na rota o valor que estava lá.