from flask import Flask
from flask import request
import boto3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '''<form action="/create" method="post">
              <p><button type="submit">Create Snapshot</button></p>
              </form>'''

# @app.route('/signin', methods=['GET'])
# def signin_form():
#     return '''<form action="/signin" method="post">
#               <p><button type="submit">Create Snapshot</button></p>
#               </form>'''

@app.route('/create', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    # if request.form['username']=='admin' and request.form['password']=='password':
    #     return '<h3>Hello, admin!</h3>'

    # print(request.form)
    ec2 = boto3.client('ec2')

    try:
        snapshot = ec2.create_snapshot(VolumeId='vol-0029918ca270ccfb0', Description='testFromPy')
        snapshot_id = snapshot['SnapshotId']
        print("快照创建成功,", snapshot_id)
        return '<h3>Create Snapshot Success</h3>' + snapshot_id
    except:
        print("快照创建错误")
        return '<h3>Create Snapshot Failure</h3>'


if __name__ == '__main__':
    app.run()