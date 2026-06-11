def test_home_status_code(client):

    response = client.get("/")

    assert response.status_code == 200