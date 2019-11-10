from flask import Flask, escape, request
from flask_cors import CORS
import json

# from zachsBaby import woot

app = Flask(__name__)
CORS(app)

# TODO Parse json data for data: ["", "", ""]
# TODO Send Paragraph to zachsBaby
# 
@app.route('/', methods=["GET", "POST"])
def hello():
    # name = request.args.get("name", "World")
    print("cors request made")
    data = "none"
    if request.method == "POST":
        data = request.data
        my_json = data.decode('utf8')#.replace("'", '"')
        data = json.loads(my_json)
        # s = json.dumps(data, indent=4, sort_keys=True)
        # print(s)
        # TODO CALL ZACHS BABY
        

    return data
    # return "Hello, {escape(name)}!"


@app.route('/test', methods=["GET", "POST"])
def test():
    text = "Donald Trump is the president. I HATE donald trump. Donald Trump is a nice guy. Donald trump can suck a dick."
    res = woot(text)
    return res
    # return "Hello, {escape(name)}!"


@app.route('/test', methods=["GET", "POST"])
def demo():
    text = "Donald Trump is the president. I HATE donald trump. Donald Trump is a nice guy. Donald trump can suck a dick."
    res = woot(text)
    return res
    # return "Hello, {escape(name)}!"


if __name__ == '__main__':
    app.run()

# To Run
# env FLASK_APP=home.py flask run
