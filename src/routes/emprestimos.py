from flask import Blueprint, render_template, jsonify
import src.services.turma_service as turma_service

bp = Blueprint("emprestimos", __name__, url_prefix="/turma")

@bp.route('/<turma>/get_emprestimos_record')
def get_emprestimos_record(turma):
    emprestimos = turma_service.get_emprestimos_record(turma)
    teste = turma_service.get_semana_atual(turma)
    print(emprestimos)
    return jsonify(teste)