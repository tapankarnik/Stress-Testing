import os
from flask import Flask, request, jsonify
import requests
import json

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
        try:
            if len(data['job_name'])>20 or len(data['job_name'])==0 or data['job_name'] == None:
                raise Exception('Invalid Job Name')
            if data['num_jobs']<0 or data['num_jobs']==0 or data['num_jobs']>100:
                raise Exception('Invalid Number of Jobs')
            if data['job_duration']<=0 or data['job_duration']>30:
                raise Exception('Invalid Job Duration')

        except Exception:
            return "Invalid Input", 400

        job_name = data['job_name']
        num_jobs = data['num_jobs']
        job_duration = data['job_duration']

        for job_id in range(num_jobs):
            # Sends POST Requests to the DCN one after the other.

            payload = {'job_name':job_name, 'job_id':job_id, 'num_jobs':num_jobs, 'job_duration':job_duration}
            url = "http://loadbalancer:5000/DCN" # IP for the DCN
            #url = "http://localhost:5006/test" # IP for the stub DCN
            
            r = requests.post(url, json=payload) # POST Request -> IP Addr of the DCN
        return b"OK", 200

    else:
        return b"Not a JSON input", 400


if __name__ == "__main__":
    print("Starting Stress Testing Suite")
    app.run(host='0.0.0.0', port=5011, debug=True)
