from flask import Blueprint, render_template
import src.services.turmas_service as turmas_service
# import src.adicionar_dados as adicionar_dados

bp = Blueprint("turmas", __name__, url_prefix="/")

'''
1 -> turmas 
2 -> cadastro
3 -> histórico 
4 -> Manual de instruções
5 -> Passagem de ano
'''

@bp.route('', methods=['GET'])
def index():
    turmas = turmas_service.get_turmas()
    return render_template('turmas.html', current_page = 1, turmas = turmas)