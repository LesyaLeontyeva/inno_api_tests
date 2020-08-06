def test_auth(auth_client):
    res = auth_client()
    assert res.status_code == 200
