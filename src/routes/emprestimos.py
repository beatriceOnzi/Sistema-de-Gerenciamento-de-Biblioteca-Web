from flask import Blueprint, render_template, request, jsonify, redirect, url_for
import src.services.emprestimos_service as emprestimos_service

bp = Blueprint("turma", __name__, url_prefix="/turma")

@bp.route('/<turma>/')
def carregar_turma(turma):
    return render_template('turma.html', current_page = 1, turma = turma)

@bp.route('/<turma>/get_emprestimos_record')
def get_emprestimos_record(turma):
    emprestimos = emprestimos_service.get_emprestimos_record(turma)
    return jsonify(emprestimos)

@bp.route('/<turma>/get_emprestimos_cadastro')
def get_emprestimos_cadastro(turma):
    new_emprestimos = emprestimos_service.get_emprestimos_cadastro(turma)
    return jsonify(new_emprestimos)

@bp.post('/<turma>/save_title')
def save_title(turma):
    data = request.get_json()

    id = data.get('id')
    titulo = data.get('title')

    emprestimos_service.save_title(id, titulo)
    return jsonify("funciona")

@bp.post('/<turma>/set_data_devolucao')
def set_data_devolucao(turma):
    data = request.get_json()

    titulo = data.get('title')
    aluno = data.get('aluno')

    emprestimos_service.set_data_devolucao(titulo, aluno, turma)
    return jsonify("funciona")

@bp.post('/<turma>/criar_semana_emprestimos')
def criar_semana_emprestimos(turma):
    nova_semana = emprestimos_service.criar_semana_emprestimos(turma)
    # retornar a semana para poder atualizar? 
    return redirect(url_for('turma.carregar_turma', turma=turma))