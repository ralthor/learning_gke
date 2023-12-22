from flask import Flask, render_template, request

from db import store_db, get_db

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('main.html')


@app.route('/health')
def health():
    return {"status": "UP"}, 200


@app.route('/store')
def store():
    key = request.args.get('key')
    value = request.args.get('value')
    try:
        store_db(key, value)
    except Exception as e:
        return {"status": "failed", "trace": e.__repr__()}, 200

    return {"key": key, "value": value}, 201


@app.route('/retrieve')
def retrieve():
    key = request.args.get('key')
    try:
        value = get_db(key)
    except Exception as e:
        return {"status": "failed", "trace": e.__repr__()}, 200

    return {"key": key, "value": value}, 200


if __name__ == '__main__':
    app.run()