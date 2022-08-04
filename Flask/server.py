import json

from flask import Flask, request, Response
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello world'


@app.route('/register', methods=['POST'])
def register():
    print(request.headers)
    # print(request.stream.read()) # 不要用，否则下面的form取不到数据
    print(request.form)
    print(request.form['name'])
    print(request.form.get('name'))
    print(request.form.getlist('name'))
    print(request.form.get('nickname', default='little apple'))
    return 'welcome'


@app.route('/add', methods=['POST'])
def add():
    print(request.headers)
    print(type(request.json))
    print(request.json)
    result = request.json['a'] + request.json['b']
    return str(result)


@app.route('/sum', methods=['POST'])
def sum():
    result = {'sum': request.json['a'] + request.json['b']}
    return Response(json.dumps(result), mimetype='application/json')


# 文件上传目录
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
# 支持的文件格式
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}  # 集合类型
# 可以限制上传文件的大小
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB


# 判断文件名是否是我们支持的格式
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route('/upload', methods=['POST'])
def upload():
    upload_file = request.files['image']
    if upload_file and allowed_file(upload_file.filename):
        filename = secure_filename(upload_file.filename)
        # 将文件保存到 static/uploads 目录，文件名同上传时使用的文件名
        upload_file.save(os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], filename))
        return 'info is ' + request.form.get('info', '') + '. success'
    else:
        return 'failed'


@app.route('/user/<username>')
def user(username):
    print(username)
    print(type(username))
    return 'hello ' + username


@app.route('/user/<username>/friends')
def user_friends(username):
    print(username)
    print(type(username))
    return 'hello ' + username

@app.route('/page/<int:num>')
def page(num):
    print(num)
    print(type(num))
    return 'hello world'


@app.route('/pages/<int:num1>-<int:num2>')
def pages(num1, num2):
    print(num1)
    print(num2)
    return 'hello world'


if __name__ == '__main__':
    app.run(port=5000, debug=True)
