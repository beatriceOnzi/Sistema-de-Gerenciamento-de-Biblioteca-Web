from src.services.aluno_service import criar_aluno


def test_carregar_turma_status_code(client):
    response = client.get("/turma/1/")
    assert response.status_code == 200


def test_get_emprestimos_record_retorna_lista_vazia(client):
    response = client.get("/turma/1/get_emprestimos_record")
    assert response.status_code == 200
    assert response.get_json() == []


def test_get_emprestimos_cadastro_retorna_lista_vazia(client):
    response = client.get("/turma/1/get_emprestimos_cadastro")
    assert response.status_code == 200
    assert response.get_json() == []


def test_avancar_semana_redireciona_para_a_turma(client):
    criar_aluno({'nome': "Aluno Rota", 'turma': 1})

    response = client.post("/turma/1/avancar_semana", follow_redirects=False)

    assert response.status_code == 302
    assert response.headers["Location"] == "/turma/1/"
