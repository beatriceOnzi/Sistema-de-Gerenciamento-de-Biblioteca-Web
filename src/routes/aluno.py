from flask import Blueprint, render_template, request, redirect, url_for, flash
from src.services.aluno_service import *

bp = Blueprint("cadastro_alunos", __name__, url_prefix="/cadastro/alunos")


@bp.route('/', methods=['GET'])
def carregar_cadastro_alunos():
    nome = request.args.get('nome', '')
    turma = request.args.get('turma', 1)
    alunos = get_alunos()
    return render_template('cadastro.html', current_page = 2, grupo = "alunos", alunos = alunos, nome = nome, turma = turma)


@bp.route('/novo', methods=['POST'])
def cadastrar_novo_aluno():
    dados = {
        'nome': request.form.get('nome_aluno'),
        'turma': (request.form.get('turma')).strip()
    }

    erros = validar_aluno(dados)
    if (erros):
        for erro in erros:
            flash(erro, 'erro')
        return redirect(url_for('cadastro_alunos.carregar_cadastro_alunos', nome = dados['nome'], turma = dados['turma']))
    
    criar_aluno(dados)
    flash("Aluno cadastrado com sucesso!", "sucesso")
    return redirect(url_for('cadastro_alunos.carregar_cadastro_alunos'), 302)


@bp.route('/delete/<int:id>', methods=['POST'])
def deletar_aluno_registrado(id):
    deletar_aluno(id)
    if not existe_aluno(id):
        flash("Aluno deletado com sucesso!", 'sucesso')
    return redirect(url_for('cadastro_alunos.carregar_cadastro_alunos'))
