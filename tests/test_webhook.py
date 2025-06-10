import json
import server


class Dummy:
    def __init__(self):
        self.calls = []

    def __call__(self, *args, **kwargs):
        self.calls.append((args, kwargs))


def test_webhook(client, monkeypatch):
    email_dummy = Dummy()
    monkeypatch.setattr(server, "send_email", email_dummy)
    response = client.post('/webhook', json={'foo': 'bar'})
    assert response.status_code == 200
    data = json.loads(response.data.decode())
    assert data['received'] == {'foo': 'bar'}
    assert email_dummy.calls, "send_email should be called"

def test_webhook_echo(client):
    response = client.post('/webhook', json={'foo': 'bar'})
    assert response.status_code == 200
    data = json.loads(response.data.decode())
    assert data['received'] == {'foo': 'bar'}

def test_invalid_json(client):
    response = client.post('/webhook', data='notjson', headers={'Content-Type': 'application/json'})
    assert response.status_code == 400
