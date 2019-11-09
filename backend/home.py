from flask import Flask, escape, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/', methods=["GET", "POST"])
def hello():
    # name = request.args.get("name", "World")
    name = "bob"
    if request.method == "POST":
        data = request.data
        print(data)
        name = data

    return name
    # return "Hello, {escape(name)}!"


# To Run
# env FLASK_APP=home.py flask run
