from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

app = Flask(__name__)
def load_file_config():
    with open("config.json") as f:
        data =json.load(f)
    return data

@app.route("/post",methods=["POST"])
def test():
    data = {"message" : "the server is running  (post)......"}
    return jsonify(data)
@app.route("/put",methods=["PUT"])
def test1():
    data = {"message" : "the server is running (put)......"}
    return jsonify(data)
@app.route("/get",methods=["GET"])
def test2():
    data = {"message" : "the server is running (get)......"}
    return jsonify(data)

if __name__ == "__main__":
    data_config = load_file_config()
    print(f"serve running : http://{data_config['url-backend']}:{data_config['port']}")
    serve(app, host=data_config["url-backend"], port=data_config["port"])

