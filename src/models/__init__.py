from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .aluno import Aluno
from .livro import Livro
from .emprestimo import Emprestimo
from .historico import Historico
from .turma import Turma