# Stress Testing Subsytem for Data Center Network

Part of the Chaos Testing Suite

[Data Center Network](https://github.com/tapankarnik/DCN)

[Stress Testing Subsystem](https://github.com/tapankarnik/Stress-Testing)

[Chaos Testing Subsystem](https://github.com/tapankarnik/Chaos-Testing)

This module is used to send job requests to the Data Center Network.

It accepts requests from the GUI with information about the jobs and sends jobs requests to the DCN.

# Docker Build

Run the following the build the docker image for the CTS

    docker build -t sts .

## Usage:

Create a virtual environment in Python3 and install the packages given in the requirements file.

Run the Flask app by 
'python3 app.py'

The server will listen on localhost:5011/jobs expecting a POST request with 3 parameters; Job Name, Number of Jobs and Job Duration.

Sample JSON

    {
        "job_name":"Solar",
        "num_jobs":8,
        "job_duration":4
    }
