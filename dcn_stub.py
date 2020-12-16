from flask import Flask, request, jsonify, render_template

dcn_stub = Flask(__name__)

@dcn_stub.route('/test', methods=['POST'])
def stub():
    if request.is_json:
        data = request.get_json()
        print(data)
        job_id = data['job_id']
        job_name = data['job_name']
        num_jobs = data['num_jobs']
        job_duration = data['job_duration']

        print('Received Job '+str(job_id)+' of '+str(num_jobs)+' under '+job_name+' for duration '+str(job_duration)+'s')
        return b'Received', 200
    else:
        print('Not JSON')
        return b'Error', 400

if __name__=="__main__":
    print("Starting the DCN Stub")
    dcn_stub.run(host='localhost', port=5006, debug=True, use_reloader=False)

