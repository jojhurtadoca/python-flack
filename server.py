from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/', methods=['GET'])
def home():
    return "Hello world!"


if (__name__ == '__main__'):
    app.run()
