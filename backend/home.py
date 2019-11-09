from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def hello():
    # name = request.args.get("name", "World")
    name = "bob"
    if request.method == "POST":
        name = "LOL"

    return name
    # return "Hello, {escape(name)}!"








# To Run
# env FLASK_APP=home.py flask run