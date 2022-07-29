from flask import Flask, jsonify, redirect

app = Flask(__name__)


@app.route("/")
def demo1():
    return "hello zy"


@app.route("/demo3")
def demo3():
    json_dict = {
        "user_id": 10,
        "user_name": "zy"
    }
    return jsonify(json_dict)

@app.route("/demo4")
def demo4():
    return redirect("http://www.baidu.com")


if __name__ == '__main__':
    app.run()
