from flask import Blueprint, jsonify, render_template, request
from models.aluno import Aluno
import services.aluno_service

bp = Blueprint("alunos", __name__, url_prefix="/") # depois separar as rotas entre Home e Turma?

@bp.route('/')
def index():
    return render_template('home.html')

@bp.route("/", methods=["POST"])
def criar():

    data = request.json

    aluno = services.aluno_service.aluno_service.criar_aluno(
        data["nome"],
        data["turma"]
    )

    return jsonify({
        "id": aluno.id,
        "nome": aluno.nome
    })

@bp.route('/alunos/', methods=['GET'])
def get_alunos():
    alunos = Aluno.query.all()
    print(alunos)
    return jsonify([{'nome': t.nome, 'turma': t.turma} for t in alunos])