def test_manual_index_status_code(client):
    response = client.get("/manualInstrucoes/")
    assert response.status_code == 200
