from flask import Flask
application = Flask(__name__)
app = application


@app.route('/')
def index():
    return 'test-api'


@app.route('/drinks')
def get_drinks():
    return {"drinks": "drink data"}

# test_commit