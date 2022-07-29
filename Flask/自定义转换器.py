from werkzeug.routing import BaseConverter
from flask import Flask

app = Flask(__name__)


class RegexConverter(BaseConverter):
    def __init__(self, url_map, regex):
        super(RegexConverter, self).__init__(url_map)
        self.regex = regex

    def to_python(self, value):
        print("to_python方法被调用")
        return value


# 将自定义的转换器添加到flask应用中
app.url_map.converters['re'] = RegexConverter


@app.route('/index/<re("123"):value>')
def index(value):
    print(value)
    return 'hello'


if __name__ == '__main__':
    app.run()
