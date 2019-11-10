from flask import Flask, escape, request
# from flask_cors import COR

from zachsBaby import woot

app = Flask(__name__)
# CORS(app)


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


@app.route('/test', methods=["GET", "POST"])
def test():
    text = "Donald Trump is the president. I HATE donald trump. Donald Trump is a nice guy. Donald trump can suck a dick."
    res = woot(text)
    return res
    # return "Hello, {escape(name)}!"


if __name__ == '__main__':
    app.run()

# To Run
# env FLASK_APP=home.py flask run