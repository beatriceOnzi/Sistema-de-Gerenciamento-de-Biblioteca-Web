from flask import Blueprint, render_template
import src.services.turmas_service as turmas_service

bp = Blueprint("historico", __name__, url_prefix="/historico")

@bp.route('/', methods=['GET'])
def index():
    return render_template('historico.html', current_page = 3)