from flask import Flask, redirect, url_for, session

app = Flask(__name__)


# Session

@app.route('/index1')
def index1(zy='zy'):
    session['username'] = zy
    return redirect(url_for('index'))


@app.route("/")
def index():
    return session.get('username')


if __name__ == '__main__':
    app.run()
