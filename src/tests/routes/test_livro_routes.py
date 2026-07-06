from src.models.livro import Livro


def test_cadastro_livro_status_code(client):
    response = client.get("/cadastro/livros")
    assert response.status_code == 308


def test_criar_livro_por_status_code(client):

    response = client.post(
        '/cadastro/livros/novo', 
        data={
            "titulo": "Título Teste"
        },
        follow_redirects = False
    )

    assert response.status_code == 302


def test_deletar_livro_status_code(client):
    client.post('/cadastro/livros/novo', data={"titulo": "Livro Deletar"})
    livro = Livro.query.filter_by(nome="Livro Deletar").first()

    response = client.post(f'/cadastro/livros/delete/{livro.id}', follow_redirects=False)

    assert response.status_code == 302
    assert Livro.query.filter_by(nome="Livro Deletar").first() is None


def test_get_livros_endpoint_retorna_nomes_cadastrados(client):
    client.post('/cadastro/livros/novo', data={"titulo": "Livro Json"})

    response = client.get('/cadastro/livros/get_livros')

    assert response.status_code == 200
    assert "Livro Json" in response.get_json()