from flask import Blueprint, render_template, request, jsonify
import src.services.turma_service as turma_service

bp = Blueprint("turma", __name__, url_prefix="/turma")

@bp.route('/<turma>/')
def carregar_turma(turma):
    alunos_turma = turma_service.get_alunos_turma(turma)
    return render_template('turma.html', current_page = 1, alunos_turma = alunos_turma, turma = turma)