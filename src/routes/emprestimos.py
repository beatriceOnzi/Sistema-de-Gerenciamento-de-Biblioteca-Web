from flask import Blueprint, render_template, request, jsonify, redirect, url_for
import src.services.emprestimos_service as emprestimos_service
import src.services.historico_service as historico_service


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

    data_devolucao = emprestimos_service.set_data_devolucao(titulo, aluno, turma)
    return jsonify(data_devolucao)

@bp.post('/<turma>/avancar_semana')
def avancar_semana(turma):
    historico_service.salvar_emprestimos(turma)
    emprestimos_service.criar_semana_emprestimos(turma)
    return redirect(url_for('turma.carregar_turma', turma=turma))