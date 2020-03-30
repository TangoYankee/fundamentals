from flask import Flask
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return "Hello, World"


@app.route('/concurrency', methods=['GET'])  # mistake: didn't close the quote
def coconcurrency():
    return "Hello, concurrency!"


if __name__ == "__main__":  # mistake: left out the colon
    app.run()
