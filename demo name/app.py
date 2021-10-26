from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World! this is Azdev india thus stay tuned and reach out to us for more gyan"
