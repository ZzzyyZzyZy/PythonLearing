from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    # 往模板中传入的数据
    my_str = 'Hello 模板'
    my_int = 1101
    my_array = [1, 2, 3, 4, 5, 6]
    my_dict = {
        'name': 'zy',
        'age': 18
    }
    return render_template('temp_demo1.html',
                           my_str=my_str,
                           my_int=my_int,
                           my_array=my_array,
                           my_dict=my_dict
                           )


if __name__ == '__main__':
    app.run()
