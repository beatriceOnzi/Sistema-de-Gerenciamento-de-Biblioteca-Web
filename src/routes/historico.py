from flask import Blueprint, render_template, jsonify, request
import src.services.emprestimos_service as emprestimo_service

bp = Blueprint("historico", __name__, url_prefix="/historico")

@bp.route('/', methods=['GET'])
def index():
    return render_template('historico.html', current_page = 3)

@bp.route('/get_historico_data', methods=['GET'])
def get_historico_data():
    all_emprestimos = emprestimo_service.get_historico_emprestimos()
    return jsonify(all_emprestimos)

@bp.post('/atualizar_data_devolucao')
def alternar_data_devolucao():
    data = request.get_json()

    id = data.get('id')

    data_devolucao = emprestimo_service.atualizar_data_devolucao_historico(id)
    return jsonify(data_devolucao)