from flask import Flask, request, make_response
from util import *
from checker import Checker

from os import listdir

app = Flask("java-autograder")

@app.route('/', methods=['POST'])
def upload():

    # Collect data from POST request
    net_ids = request.form['netids'].split('_')
    folder_name = request.form['group_id']
    file_name = request.form['file_name_0']
    assignment = request.form['assignment_name']
    submission = request.files[file_name] 
    
    # Create temporary directory and save submission
    folder_name = path(folder_name)
    mkdir(folder_name)
    file_name = add_ext(file_name, ".zip")
    submission.save(file_name)
    extract(file_name, folder_name)

    # Check submission
    checker = Checker(assignment, folder_name)
    print(checker.check())

    # Clean up
    rmdir(folder_name)
    return make_response("Success")

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
