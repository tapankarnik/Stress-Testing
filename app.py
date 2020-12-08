import os
from flask import Flask, request, jsonify, render_template
import requests
import pytest

app = Flask(__name__)

@app.route('/jobs', methods=['POST'])
def gen_jobs():
    """
    Receives information on batch of jobs.
    Params:
    JSON with attributes:
    job_name - str
    num_jobs - int
    job_duration - int
    """
    if request.is_json:
        data = request.get_json()
        job_name = data['job_name']
        num_jobs = data['num_jobs']
        job_duration = data['job_duration']

        for job_id in range(num_jobs):
            # Sends POST Requests to the DCN one after the other.

            payload = {'job_name':job_name, 'job_id':job_id, 'total_jobs':num_jobs, 'job_duration':job_duration}
            r = requests.post('https://www.google.com',params=payload) # POST Request -> IP Addr of the DCN
        return b"OK", 200
    else:
        return b"Not a JSON input", 400


if __name__ == "__main__":
    print("Starting Stress Testing Suite")
    app.run(debug=True, use_reloader=False, threaded=False)
