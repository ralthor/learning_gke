from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/health')
def health():
    return {"status": "UP"}, 200


if __name__ == '__main__':
    app.run()