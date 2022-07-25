#flask路由
from flask import Flask
app = Flask(__name__)  #实例化

@app.route('/hello')
def hello():
    return 'hello world'

@app.route('/hellos')
def hellos():
    return 'hello worlds'

@app.route('/hello1',methods = ['GET','POST'])
def hello1():
    return 'hello world'

@app.route('/hello2',methods = ['POST'])
def hello2():
    return 'hello worldss'

@app.route('/user/<id>')
def index(id):
    if id == '1':
        return 'hello zy'
    if id == '2':
        return 'hello zzzy'


if __name__ == '__main__':
    app.run()
