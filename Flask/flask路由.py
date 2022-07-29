# flask路由
from flask import Flask, url_for, render_template, request, make_response,abort,redirect

app = Flask(__name__)  # 实例化


@app.route('/hello')
def hello():
    return 'hello world'


@app.route('/hellos')
def hellos():
    return 'hello worlds'


@app.route('/hello1', methods=['GET', 'POST'])
def hello1():
    return 'hello world'


@app.route('/hello2', methods=['POST'])
def hello2():
    return 'hello worldss'


@app.route('/user/<id>')
def index(id):
    if id == '1':
        return 'hello zy'
    if id == '2':
        return 'hello zzzy'


# 如果输入/project 会自动补全为 /project/  重定向行为
@app.route("/project/")
def projects():
    return 'The project page'


# 如果如果/about/ 则会报错404
@app.route("/about")
def about():
    return 'The about page'


@app.route('/zzy/')
@app.route('/zzy/<name>')
def zzy(name=None):
    return render_template("hello.html", name=name)


# @app.route('/login',methods=['POST','GET'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if valid_login(request.form['username'],
#                        request.form['password']):
#             return log_the_user_in(request.form['username'])
#         else:
#             error = 'Invalid username/password'
#             # the code below is executed if the request method
#             # was GET or the credentials were invalid
#         return render_template('login.html', error=error)

##Cookies

###读取Cookies
# @app.route('/')
# def indexcookie():
#     username = request.cookies.get('username')


###存储Cookies
# @app.route('/')
# def indexCookies():
#     resp = make_response(render_template(...))
#     resp.set_cookie('username', 'the username')
#     return resp

#Flask重定向和错误
app.route('/')
def index1():
    return redirect(url_for('login'))

app.route('/login')
def login():
    abort(401)

##

@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('error.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp


if __name__ == '__main__':
    app.run()
