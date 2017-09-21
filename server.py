from flask import Flask, request
from util import *

app = Flask("java-autograder")

@app.route('/', methods=['POST'])
def upload():

    # Collect data from POST request
    net_ids = request.form['netids'].split('_')
    folder_name = request.form['group_id']
    file_name = request.form['file_name_0']
    assignment = request.form['assignment_id']
    submission = request.files[file_name] 
    
    # Create temporary directory and save submission
    folder_name = path(folder_name)
    mkdir(folder_name)

    file_name = folder_name + "/" + file_name + ".zip"
    submission.save(file_name)

    rm(folder_name)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
