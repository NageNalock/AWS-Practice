from flask import request
from flask import Flask
import boto3
# from werkzeug import secure_filename

app = Flask(__name__)

@app.route('/', methods=['GET'])
def signin_form():
    return '''<form action="/upload" method="post" enctype="multipart/form-data">
              <p><input type="file" name="the_file" >
              <p><button type="submit">upload</button></p>
              </form>'''

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    file_name = 'uploaded_file'
    if request.method == 'POST':
        f = request.files['the_file']
        f.save(file_name)

    s3 = boto3.resource('s3')
    # file_name = '11hello.txt'
    s3.Object('start.demo', file_name).put(Body=open(file_name, 'rb'))
    #print(s3.Object('start.demo', '11hello.txt'))
    print('https://s3.us-east-2.amazonaws.com/start.demo/' + file_name)
    return '文件上传成功' + '<a>'+'https://s3.us-east-2.amazonaws.com/start.demo/'  +file_name+'</a>'



if __name__ == '__main__':
    app.run()