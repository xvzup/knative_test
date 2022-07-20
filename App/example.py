import json                                                     
import os
from flask import Flask, request
from werkzeug.utils import secure_filename

app = Flask(__name__)                                           

@app.route('/test_api',methods=['GET','POST'])            
def test_api():                                           
    uploaded_file = request.files['document']
    data = json.load(request.files['data'])
    filename = secure_filename(uploaded_file.filename)
    uploaded_file.save(os.path.join('path/where/to/save', filename))
    print(data)
    return 'success'

if __name__ == '__main__':
    app.run(host='localhost', port=8080)