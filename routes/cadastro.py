from flask import Blueprint, render_template, request, redirect, url_for
from services.aluno_service import *
from services.livro_service import *

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
    novoAluno(nome_aluno, turma)
    return redirect(url_for('cadastro.carregar_cadastro_alunos'))


@bp.route('/alunos/delete/<int:id>', methods=['POST'])
def deletar_aluno(id):
    deleteAluno({id})
    return redirect(url_for('cadastro.carregar_cadastro_alunos'))

# Livros
@bp.route('/livros/', methods=['GET'])
def carregar_cadastro_livros():
    livros = get_livros()
    return render_template('cadastro.html', current_page = 2, grupo = "livros", livros = livros)

@bp.route('/livros/novo', methods=['POST'])
def cadastrar_novo_livro():
    titulo = request.form.get('titulo')
    novoLivro(titulo)
    return redirect(url_for('cadastro.carregar_cadastro_livros'))

@bp.route('/livros/delete/<int:id>', methods=['POST'])
def deletar_livro(id):
    deleteLivro({id})
    return redirect(url_for('cadastro.carregar_cadastro_livros'))