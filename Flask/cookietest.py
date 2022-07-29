from flask import Flask, make_response, request, session, redirect, url_for

app = Flask(__name__)


# 设置cookie
@app.route('/cookie')
def set_cookie():
    resp = make_response("this is to set cookie")
    resp.set_cookie('username', 'zy', max_age=20)
    return resp


# 获取cookie
@app.route('/request')
def resp_cookie():
    resp = request.cookies.get('username')
    return resp



if __name__ == '__main__':
    app.run()
