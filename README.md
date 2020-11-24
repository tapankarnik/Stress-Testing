# Stress Testing Subsytem

This module is used to send job requests to the Data Center Network.

It accepts requests from the GUI with information about the jobs and sends jobs requests to the DCN.

## Usage:
Create a virtual environment in Python3 and install the packages given in the requirements file.

Run the Flask app by 
'python3 app.py'

The server will listen on port 5000 expecting a POST request with 3 parameters; Job Name, Number of Jobs and Job Duration.
