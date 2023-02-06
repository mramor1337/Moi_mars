from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Миссия Колонизация Марса</h1>"


@app.route('/index')
def my_second_index():
    return "<h2>И на Марсе будут яблони цвести!</h2>"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
