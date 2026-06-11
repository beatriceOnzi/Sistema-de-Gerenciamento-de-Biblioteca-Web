def test_cadastro_alunos_status_code(client):
    response = client.get("/cadastro/alunos")
    assert response.status_code == 308 

def test_criar_aluno_por_status_code(client):

    response = client.post(
        '/cadastro/alunos/novo', 
        data={
            "nome_aluno": "Nome Teste", 
            "turma": 2
        },
        follow_redirects=True
    )

    assert response.status_code == 201
