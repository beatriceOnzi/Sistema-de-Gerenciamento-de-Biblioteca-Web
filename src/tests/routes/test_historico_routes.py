def test_historico_index_status_code(client):
    response = client.get("/historico/")
    assert response.status_code == 200
