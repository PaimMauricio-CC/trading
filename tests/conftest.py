import os
import sys
import pytest

# ensure server module can be imported when tests are run from repo root
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from server import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
