from flask import request
from flask import Flask
import boto3
from werkzeug.utils import secure_filename

app = Flask(__name__)



@app.route('/', methods=['GET'])
def signin_form():
    return '''<form action="/upload" method="post" enctype="multipart/form-data">
              <p><input type="file" name="the_file" >
              <p><button type="submit">Upload</button></p>
              </form>'''


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    bucket_name = "start.demo"
    try:
        if request.method == 'POST':
            f = request.files['the_file']
            file_name = f.filename
            # file_name = secure_filename(f.filename)  # 安全的获取文件原名,但是无法识别中文,只能改源码
            print(file_name)

            # 废弃方法
            # f.save(file_name)
            # # file_name = '11hello.txt'
            # s3.Object('start.demo', file_name).put(Body=open(file_name, 'rb'))

            s3 = boto3.client('s3')
            s3.upload_fileobj(f, bucket_name, file_name)

            # 获取下载地址
            url = s3.generate_presigned_url(
                ClientMethod='get_object',
                Params={
                    'Bucket': bucket_name,
                    'Key': file_name
                }
            )

            print(url)
            # print(s3.Object('start.demo', '11hello.txt'))
            return '''<form action="/check" method="post">
              <p><button type="submit" value="''' + url + '''" name="check">Check</button></p>
              </form>'''
        else:
            return 'File Upload Failed'
    except:
        print('错误')
        return 'File Upload Failed'


@app.route('/check', methods=['GET', 'POST'])
def check_file_link():
    # print("form:", request.form["check"])
    url = request.form["check"]

    return '<p>Donwload Link</p>' \
           '<a href="' + url +'">' + url + '</a>'


def charge(judge):
    if judge == 'Y':
        app.run(host='0.0.0.0')
    elif judge == 'N':
        app.run()
    else:
        new_judge = input('输入出错,请重新输入(Y/N)')
        charge(new_judge)


if __name__ == '__main__':
    judge = input('是否允许外部访问(Y/N)')
    charge(judge)