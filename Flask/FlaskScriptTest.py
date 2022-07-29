from flask import Flask
from flask_script import Manager

app = Flask(__name__)

manger = Manager(app)


@app.route('/')
def index():
    return 'hello Zy'


if __name__ == '__main__':
    manger.run()
