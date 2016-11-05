from flask import Flask, request, redirect, url_for
import flask
from flask.ext.cors import CORS
import os
import json
import logging
import zipfile
import utils
import time
from werkzeug.utils import secure_filename

#logging.basicConfig(filename='/var/www/flaskserver/log/server.log',level=logging.INFO)
logging.getLogger('flask_cors').level = logging.INFO

#TODO Upload folder. You need to create it first, or specify the existing one
UPLOAD_FOLDER = '/home/igor/imgs'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])



app = Flask(__name__)

#addin an upload folder
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)


@app.route('/')
def home():
    return "Home sweet home"


@app.route('/test')
def test():
    return "Test a route: Success!!"




#ADDED PART
almost_a_db = {}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

# Route that will process the file upload
@app.route('/upload', methods=['POST', 'GET'])
def upload():

    if request.method == 'POST':
        # Get the name of the uploaded file
        file = request.files['file']
        username = request.form['username']

        # Check if the file is one of the allowed types/extensions
        if file and allowed_file(file.filename):
            # Make the filename safe, remove unsupported chars
            filename = secure_filename(file.filename)

            #Creating a unic Id
            unic_id = utils.id_generator()
            #Saving username and filename for the file

            #Zipping and saving the uploaded file
            zf = zipfile.ZipFile(os.path.join(app.config['UPLOAD_FOLDER'], unic_id+'.zip'), mode='w')
            zf.write(filename)
            zf.close()

            almost_a_db[unic_id] = (filename, username, time.ctime(int(time.time())),
                                    str(os.stat(os.path.join(app.config['UPLOAD_FOLDER'], unic_id+'.zip')).st_size)+' bytes')

            return unic_id

    else:
        return """
            <!doctype html>
            <title>Upload new File</title>
            <h1>Upload new File</h1>
            <form action="" method=post enctype=multipart/form-data>
              <p><input type=file name=file>
                 <input type=submit value=Upload>
            </form>
            <p>%s</p>
            """ % "<br>".join(os.listdir(app.config['UPLOAD_FOLDER'], ))

@app.route('/retrieve', methods=['GET'])
def retrieve():
    if request.method == 'GET':
        unic_id = request.form['unic_id']

        try:
            return flask.send_from_directory(app.config['UPLOAD_FOLDER'],unic_id+'.zip')
        except Exception as e:
            return "Your file hasn't been zipped yet"
    return "Unsupported API method"

@app.route('/listing', methods=['GET'])
def get_listing():

    return json.dumps([value for value in almost_a_db.values()])


@app.route('/unzip', methods=['GET'])
def get_unzipped():
    if request.method == 'GET':
        unic_id = request.form['unic_id']

        zf = zipfile.ZipFile(os.path.join(app.config['UPLOAD_FOLDER'], unic_id+'.zip'),"r")
        l = zf.extractall(app.config['UPLOAD_FOLDER'])
        zf.close()

        #response = {flask.send_from_directory(app.config['UPLOAD_FOLDER'],almost_a_db[unic_id][0]),
        #            almost_a_db[unic_id][0].rsplit('.', 1)[1]}

        return flask.send_from_directory(app.config['UPLOAD_FOLDER'],almost_a_db[unic_id][0])
    return "Unsupported API method"

if __name__ == '__main__':
    app.run(debug=True)
