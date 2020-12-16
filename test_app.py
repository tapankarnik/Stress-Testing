from app_sliced import app

import pytest
import json

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_app1_valid_input(client):
    payload = dict(
        job_name = "Tapan",
        num_jobs = 12,
        job_duration = 2,
        )
    payload = json.dumps(payload)
    result = client.post('/jobs', data=payload, content_type='application/json')
    assert b"OK" in result.data

def test_app2_invalid_jobname_1(client):
    payload = dict(
        job_name = None,
        num_jobs = 2,
        job_duration = 2,
        )
    payload = json.dumps(payload)
    result = client.post('/jobs', data=payload, content_type='application/json')
    assert b"Invalid Input" in result.data

def test_app3_invalid_jobname_2(client):
    payload = dict(
        job_name = "",
        num_jobs = 2,
        job_duration = 2,
        )
    payload = json.dumps(payload)
    result = client.post('/jobs', data=payload, content_type='application/json')
    assert b"Invalid Input" in result.data

def test_app4_invalid_numjobs_1(client):
    payload = dict(
        job_name = "Tapan",
        num_jobs = 0,
        job_duration = 15,
        )
    payload = json.dumps(payload)
    result = client.post('/jobs', data=payload, content_type='application/json')
    assert b"Invalid Input" in result.data

def test_app5_invalid_jobname_3(client):
    payload = dict(
        job_name = "j-1234858585858585858588585948359348594385983",
        num_jobs = 50,
        job_duration = 2,
        )
    payload = json.dumps(payload)
    result = client.post('/jobs', data=payload, content_type='application/json')
    assert b"Invalid Input" in result.data

def test_app6_invalid_numjobs_2(client):
    payload = dict(
        job_name = "Tapan",
        num_jobs = 101,
        job_duration = 29,
        )
    payload = json.dumps(payload)
    result = client.post('/jobs', data=payload, content_type='application/json')
    assert b"Invalid Input" in result.data

def test_app7_invalid_jobduration_1(client):
    payload = dict(
        job_name = "Tapan",
        num_jobs = 99,
        job_duration = 0,
        )
    payload = json.dumps(payload)
    result = client.post('/jobs', data=payload, content_type='application/json')
    assert b"Invalid Input" in result.data

def test_app8_invalid_jobduration_2(client):
    payload = dict(
        job_name = "Tapan",
        num_jobs = 100,
        job_duration = 31,
        )
    payload = json.dumps(payload)
    result = client.post('/jobs', data=payload, content_type='application/json')
    assert b"Invalid Input" in result.data

