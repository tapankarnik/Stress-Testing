from app import app

import pytest
import json

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_app1(client):
    payload = dict(
        job_name = "Tapan",
        num_jobs = 12,
        job_duration = 2,
        )
    payload = json.dumps(payload)
    result = client.post('/jobs', data=payload, content_type='application/json')
    assert b"OK" in result.data


