from app import app

def test_hello():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    from app import app

def test_hello_status():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

def test_hello_contenu():
    client = app.test_client()
    response = client.get('/')
    assert b"Mon premier serveur" in response.data

def test_route_inexistante():
    client = app.test_client()
    response = client.get('/pagedoesnotexist')
    assert response.status_code == 404
