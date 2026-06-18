from flask import Blueprint, render_template, request, redirect, url_for, flash
from src.services.aluno_service import *
from src.services.livro_service import *

bp = Blueprint("cadastro_livros", __name__, url_prefix="/cadastro/livros")

@bp.route('/', methods=['GET'])
def carregar_cadastro_livros():
    titulo = request.args.get('titulo', '')
    livros = get_livros()
    return render_template('cadastro.html', current_page = 2, grupo = "livros", livros = livros, titulo=titulo)

@bp.route('/novo', methods=['POST'])
def cadastrar_novo_livro():
    titulo = request.form.get('titulo')

    erros = validar_livro(titulo)
    if (erros):
        for erro in erros:
            flash(erro, 'erro')
        return redirect(url_for('cadastro_livros.carregar_cadastro_livros', titulo=titulo))
    
    criar_livro(titulo)
    flash("Livro cadastrado com sucesso!", "sucesso")
    return redirect(url_for('cadastro_livros.carregar_cadastro_livros'), code=302 )

@bp.route('/delete/<int:id>', methods=['POST'])
def deletar_livro_registrado(id):
    deletar_livro(id)
    flash("Livro deletado com sucesso!", "sucesso")
    return redirect(url_for('cadastro_livros.carregar_cadastro_livros'))