from flask import Blueprint, render_template, jsonify, request
import src.services.historico_service as historico_service

bp = Blueprint("historico", __name__, url_prefix="/historico")

@bp.route('/', methods=['GET'])
def index():
    return render_template('historico.html', current_page = 3)

@bp.route('/get_historico_data', methods=['GET'])
def get_historico_data():
    all_emprestimos = historico_service.get_historico()
    return jsonify(all_emprestimos)

@bp.post('/atualizar_data_devolucao')
def alternar_data_devolucao():
    data = request.get_json()

    id = data.get('id')

    data_devolucao = historico_service.set_data_devolucao(id)
    return jsonify(data_devolucao)