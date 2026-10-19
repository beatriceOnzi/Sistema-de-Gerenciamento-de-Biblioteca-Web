"""
Migra os dados do banco antigo (biblioteca.db, SQLite) para o banco novo
definido em models/ (Flask-SQLAlchemy / PostgreSQL).

Coloque este arquivo na raiz do projeto (junto de config.py e da pasta models/).

Uso:
    python migrar_dados.py --origem biblioteca.db --dry-run     # simula, não grava
    python migrar_dados.py --origem biblioteca.db               # migra de verdade

    # opcional: informar o destino manualmente (senão usa DATABASE_URL do .env)
    python migrar_dados.py --origem biblioteca.db --destino postgresql+psycopg2://user:senha@localhost:5432/cnec_biblioteca_db

Regras de conversão:
  - turma "1º Ano" -> 1 (Turma.turma_formatada guarda o texto original "1º Ano")
  - aluno com turma vazia (era do 9º Ano e foi "avançado") -> turma = NULL, status = False
  - demais alunos -> status = True
  - datas dd/mm/aaaa (ou aaaa-mm-dd) -> Date
  - emprestimos.data_devolucao_real -> Emprestimo.data_devolucao
  - Emprestimo.livro_nome é preenchido com o nome do livro
  - os IDs são gerados pelo banco novo; as relações (aluno_id, livro_id) são remapeadas
  - rodar duas vezes não duplica registros (alunos, livros, turmas e empréstimos já existentes são pulados)
"""
import argparse
import re
import sqlite3
import sys
from datetime import date, datetime


# ----------------------------------------------------------------------
# Funções de conversão
# ----------------------------------------------------------------------
def parse_turma(valor):
    """'1º Ano' -> 1.  Vazio/None/sem número -> None."""
    if valor is None:
        return None
    if isinstance(valor, int):
        return valor
    m = re.search(r"\d+", str(valor))
    return int(m.group()) if m else None


def parse_data(valor):
    """'dd/mm/aaaa' ou 'aaaa-mm-dd' -> date. Vazio/inválido -> None."""
    if valor is None:
        return None
    s = str(valor).strip()
    if not s:
        return None
    for fmt in ("%d/%m/%Y", "%Y-%m-%d", "%Y-%m-%d %H:%M:%S"):
        try:
            return datetime.strptime(s, fmt).date()
        except ValueError:
            continue
    return None


def parse_int(valor):
    """Converte para int; se não der (ex.: data salva por engano), retorna None."""
    try:
        return int(valor)
    except (TypeError, ValueError):
        return None


# ----------------------------------------------------------------------
# Migração
# ----------------------------------------------------------------------
def migrar(origem_path, destino_uri, dry_run=False):
    # imports aqui dentro para as funções acima poderem ser testadas isoladamente
    from flask import Flask
    from src.models import db, Aluno, Livro, Emprestimo, Turma

    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = destino_uri
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    src = sqlite3.connect(origem_path)
    src.row_factory = sqlite3.Row

    resumo = {
        "turmas": 0, "livros": 0, "alunos": 0, "emprestimos": 0,
        "puladas": 0, "avisos": [],
    }

    with app.app_context():
        # cria somente tabelas que ainda não existem (não altera as existentes)
        db.create_all()

        try:
            # ---------------- TURMAS (config_turma) ----------------
            for r in src.execute("SELECT turma, semana_atual FROM config_turma"):
                num = parse_turma(r["turma"])
                if num is None:
                    resumo["avisos"].append(f"config_turma ignorada (turma inválida): {r['turma']!r}")
                    continue
                semana = parse_int(r["semana_atual"])
                if semana is None:
                    resumo["avisos"].append(
                        f"turma {r['turma']!r}: semana_atual {r['semana_atual']!r} não é número, usando 1")
                    semana = 1

                t = db.session.get(Turma, num)
                if t is None:
                    db.session.add(Turma(turma=num, turma_formatada=str(r["turma"]).strip(),
                                         semana_atual=semana))
                    resumo["turmas"] += 1
                else:
                    resumo["puladas"] += 1

            # turmas usadas por alunos/empréstimos mas ausentes em config_turma
            usadas = set()
            for tabela in ("alunos", "emprestimos"):
                for r in src.execute(f"SELECT DISTINCT turma FROM {tabela}"):
                    usadas.add(r["turma"])
            for texto in usadas:
                num = parse_turma(texto)
                if num is not None and db.session.get(Turma, num) is None:
                    db.session.add(Turma(turma=num, turma_formatada=str(texto).strip(), semana_atual=1))
                    resumo["turmas"] += 1
                    resumo["avisos"].append(f"turma {texto!r} não estava em config_turma; criada com semana 1")
            db.session.flush()

            # ---------------- LIVROS ----------------
            mapa_livros = {}   # id antigo -> id novo
            nomes_livros = {}  # id antigo -> nome
            for r in src.execute("SELECT id, nome FROM livros ORDER BY id"):
                nome = r["nome"].strip()
                livro = Livro.query.filter_by(nome=nome).first()
                if livro is None:
                    livro = Livro(nome=nome)
                    db.session.add(livro)
                    db.session.flush()
                    resumo["livros"] += 1
                else:
                    resumo["puladas"] += 1
                mapa_livros[r["id"]] = livro.id
                nomes_livros[r["id"]] = nome

            # ---------------- ALUNOS ----------------
            mapa_alunos = {}  # id antigo -> id novo
            for r in src.execute("SELECT id, nome, turma FROM alunos ORDER BY id"):
                nome = r["nome"].strip()
                turma_num = parse_turma(r["turma"])
                texto_turma = (r["turma"] or "").strip()

                # turma vazia = aluno que saiu do 9º ano -> inativo
                ativo = bool(texto_turma) and turma_num is not None
                if texto_turma and turma_num is None:
                    resumo["avisos"].append(f"aluno {nome!r}: turma {texto_turma!r} inválida, ficou sem turma/inativo")

                aluno = Aluno.query.filter_by(nome=nome, turma=turma_num).first()
                if aluno is None:
                    aluno = Aluno(nome=nome, turma=turma_num, status=ativo)
                    db.session.add(aluno)
                    db.session.flush()
                    resumo["alunos"] += 1
                else:
                    resumo["puladas"] += 1
                mapa_alunos[r["id"]] = aluno.id

            # ---------------- EMPRÉSTIMOS ----------------
            for r in src.execute("SELECT * FROM emprestimos ORDER BY id"):
                aluno_id = mapa_alunos.get(r["aluno_id"])
                if aluno_id is None:
                    resumo["avisos"].append(f"empréstimo {r['id']} ignorado: aluno {r['aluno_id']} não existe")
                    continue

                livro_id = mapa_livros.get(r["livro_id"])  # None se o livro foi excluído (FK SET NULL)
                data_emp = parse_data(r["data_emprestimo"])
                semana = parse_int(r["semana"])

                ja_existe = Emprestimo.query.filter_by(
                    aluno_id=aluno_id, livro_id=livro_id,
                    data_emprestimo=data_emp, semana=semana,
                ).first()
                if ja_existe:
                    resumo["puladas"] += 1
                    continue

                turma_num = parse_turma(r["turma"])
                if turma_num is None:
                    # empréstimo antigo sem turma: usa a turma atual do aluno, se houver
                    turma_num = db.session.get(Aluno, aluno_id).turma

                db.session.add(Emprestimo(
                    aluno_id=aluno_id,
                    livro_id=livro_id,
                    livro_nome=nomes_livros.get(r["livro_id"]),
                    data_emprestimo=data_emp,
                    data_devolucao_prevista=parse_data(r["data_devolucao_prevista"]),
                    data_devolucao=parse_data(r["data_devolucao_real"]),
                    turma=turma_num,
                    semana=semana,
                ))
                resumo["emprestimos"] += 1

            if dry_run:
                db.session.rollback()
            else:
                db.session.commit()

        except Exception:
            db.session.rollback()
            raise
        finally:
            src.close()

    return resumo


def main():
    ap = argparse.ArgumentParser(description="Migra biblioteca.db (antigo) para o banco novo (models/).")
    ap.add_argument("--origem", default="biblioteca.db", help="caminho do SQLite antigo")
    ap.add_argument("--destino", default=None, help="URI do banco novo (padrão: DATABASE_URL do .env)")
    ap.add_argument("--dry-run", action="store_true", help="simula tudo e desfaz no final")
    args = ap.parse_args()

    destino = args.destino
    if not destino:
        from config import Config
        destino = Config.SQLALCHEMY_DATABASE_URI
    if not destino:
        sys.exit("DATABASE_URL não definida. Use --destino ou configure o .env.")

    r = migrar(args.origem, destino, dry_run=args.dry_run)

    print("\n=== DRY-RUN (nada foi gravado) ===" if args.dry_run else "\n=== Migração concluída ===")
    print(f"Turmas inseridas:      {r['turmas']}")
    print(f"Livros inseridos:      {r['livros']}")
    print(f"Alunos inseridos:      {r['alunos']}")
    print(f"Empréstimos inseridos: {r['emprestimos']}")
    print(f"Já existentes (pulados): {r['puladas']}")
    if r["avisos"]:
        print("\nAvisos:")
        for a in r["avisos"]:
            print("  -", a)


if __name__ == "__main__":
    main()
