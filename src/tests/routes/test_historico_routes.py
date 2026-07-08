import src.services.historico_service as historico_service
import src.services.emprestimos_service as emprestimo_service

def test_historico_index_status_code(client):
    response = client.get("/historico/")
    assert response.status_code == 200

def test_get_historico_status_code(client):
    response = client.get("/historico/get_historico_data")
    assert response.status_code == 200

