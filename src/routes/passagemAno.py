from flask import Blueprint, render_template, jsonify
import src.services.passagemAno_service as passagemAno_service

bp = Blueprint("passagemAno", __name__, url_prefix="/passagemAno")

@bp.route('/', methods=['GET'])
def index():
    return render_template('passagemAno.html', current_page = 5)

@bp.route('/avancarAno', methods=['GET'])
def avancarAno():
    print("rota")
    mensagem = passagemAno_service.avancar_turmas()
    return jsonify(mensagem)