from flask import Flask, request
import os
import shutil

app = Flask("java-autograder")

@app.route('/', methods=['POST'])
def upload():

    net_ids = request.form['netids'].split('_')
    print(net_ids)
    folder_name = request.form['group_id']
    print(folder_name)
    file_name = request.form['file_name_0']
    print(file_name)
    submission = request.files[file_name] 
    
    folder_name = os.path.join(os.getcwd(), folder_name)
    os.mkdir(folder_name) 

    submission.save(folder_name + "/" + file_name)

    print(os.listdir(os.getcwd()))
    print(os.listdir(folder_name))

    shutil.rmtree(folder_name)

    print(folder_name + "exists: " + str(os.path.exists(os.path.join(os.getcwd(), folder_name))))

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
