from flask import Blueprint, render_template
import src.services.home_service as home_service
import src.adicionar_dados as adicionar_dados

bp = Blueprint("home", __name__, url_prefix="/")

'''
1 -> turmas 
2 -> cadastro
3 -> histórico 
4 -> Manual de instruções
5 -> Passagem de ano
'''

@bp.route('', methods=['GET'])
def index():
    turmas = home_service.get_turmas()
    return render_template('turmas.html', current_page = 1, turmas = turmas)