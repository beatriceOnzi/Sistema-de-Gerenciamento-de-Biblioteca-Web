from flask import Blueprint, render_template, request, jsonify
import src.services.emprestimos_service as emprestimos_service

bp = Blueprint("turma", __name__, url_prefix="/turma")

@bp.route('/<turma>/')
def carregar_turma(turma):
    alunos_turma = emprestimos_service.get_alunos_turma(turma)
    return render_template('turma.html', current_page = 1, alunos_turma = alunos_turma, turma = turma)

@bp.route('/<turma>/get_emprestimos_record')
def get_emprestimos_record(turma):
    emprestimos = emprestimos_service.get_emprestimos_record(turma)
    print(f'emprestimos rota {emprestimos}')
    return jsonify(emprestimos)