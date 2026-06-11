from flask import Blueprint, render_template, request, redirect, url_for, flash
from src.services.aluno_service import *
from src.services.livro_service import *

bp = Blueprint("cadastro", __name__, url_prefix="/cadastro")

'''
1 -> turmas 
2 -> cadastro
3 -> histórico 
4 -> Manual de instruções
5 -> Passagem de ano
'''

# Alunos
@bp.route('/alunos/', methods=['GET'])
def carregar_cadastro_alunos():
    alunos = get_alunos()
    return render_template('cadastro.html', current_page = 2, grupo = "alunos", alunos = alunos)


@bp.route('/alunos/novo', methods=['POST'])
def cadastrar_novo_aluno():
    nome_aluno = request.form.get('nome_aluno')
    turma = request.form.get('turma')

    erros = validar_aluno(nome_aluno, turma)
    if (erros):
        for erro in erros:
            flash(erro, 'erro')
        return redirect(url_for('cadastro.carregar_cadastro_alunos'))
    
    criar_aluno(nome_aluno, turma)
    flash("Aluno cadastrado com sucesso!", "sucesso")
    return redirect(url_for('cadastro.carregar_cadastro_alunos')), 201


@bp.route('/alunos/delete/<int:id>', methods=['POST'])
def deletar_aluno_registrado(id):
    deletar_aluno(id)
    #testar se deletou
    flash("Aluno deletado com sucesso!", 'sucesso')
    return redirect(url_for('cadastro.carregar_cadastro_alunos'))

# Livros
@bp.route('/livros/', methods=['GET'])
def carregar_cadastro_livros():
    livros = get_livros()
    return render_template('cadastro.html', current_page = 2, grupo = "livros", livros = livros)

@bp.route('/livros/novo', methods=['POST'])
def cadastrar_novo_livro():
    titulo = request.form.get('titulo')

    erros = validar_livro(titulo)
    if (erros):
        for erro in erros:
            flash(erro, 'erro')
        return redirect(url_for('cadastro.carregar_cadastro_livros'))
    
    criar_livro(titulo)
    flash("Livro cadastrado com sucesso!", "sucesso")
    return redirect(url_for('cadastro.carregar_cadastro_livros')), 201

@bp.route('/livros/delete/<int:id>', methods=['POST'])
def deletar_livro_registrado(id):
    deletar_livro(id)
    flash("Livro deletado com sucesso!", "sucesso")
    return redirect(url_for('cadastro.carregar_cadastro_livros'))