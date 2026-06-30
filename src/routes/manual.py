from flask import Blueprint, render_template

bp = Blueprint("manual", __name__, url_prefix="/manualInstrucoes")

@bp.route('/', methods=['GET'])
def index():
    return render_template('manual.html', current_page = 4)