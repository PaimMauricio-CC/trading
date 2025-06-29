import json
import server


def test_webhook(client):
    response = client.post('/webhook', json={'foo': 'bar'})
    assert response.status_code == 200
    data = json.loads(response.data.decode())
    assert data['received'] == {'foo': 'bar'}

def test_invalid_json(client):
    response = client.post('/webhook', data='notjson', headers={'Content-Type': 'application/json'})
    assert response.status_code == 400


def test_webhook_prints_to_console(client, monkeypatch):
    printed = []

    def fake_print(*args, **kwargs):
        printed.append(' '.join(str(a) for a in args))

    monkeypatch.setattr('builtins.print', fake_print)
    response = client.post('/webhook', json={'foo': 'bar'})
    assert response.status_code == 200
    assert any('Received alert' in p for p in printed)
