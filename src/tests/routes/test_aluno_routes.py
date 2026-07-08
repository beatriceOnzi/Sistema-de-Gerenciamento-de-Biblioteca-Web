import src.services.aluno_service as service

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
        follow_redirects = False
    )

    assert response.status_code == 302


def test_criar_aluno_invalido_redireciona_com_erro(client):
    response = client.post(
        '/cadastro/alunos/novo',
        data={
            "nome_aluno": "ab",
            "turma": 2
        },
        follow_redirects=False
    )

    assert response.status_code == 302


def test_deletar_aluno_status_code(client):
    client.post(
        '/cadastro/alunos/novo',
        data={"nome_aluno": "Aluno Deletar", "turma": 2}
    )
    aluno = service.get_aluno_by_nome("Aluno Deletar")

    response = client.post(f'/cadastro/alunos/delete/{aluno.id}', follow_redirects=False)

    assert response.status_code == 302
    assert service.get_aluno_by_nome("Aluno Deletar") is None