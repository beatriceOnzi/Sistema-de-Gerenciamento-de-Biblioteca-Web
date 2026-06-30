from src.models import db, Emprestimo, Historico

class HistoricoRepository:
    def salvar_emprestimos(self, emprestimos):
        # se nao tiver tiver livro -> nao salvar 
        print("teste ", emprestimos)
        return "teste"