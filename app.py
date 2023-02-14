from flask import Flask

app = Flask(__name__)

@app.route("/")

def hello_world():
    return "Hello world!"


@app.route("/faq")

def faq():
    return "Frequently asked questions."