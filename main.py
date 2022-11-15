from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
from controller.estudiante_controller import ControladorEstudiante
app = Flask(__name__)
estudiante_controller = ControladorEstudiante()
def load_file_config():
    with open("config.json") as f:
        data =json.load(f)
    return data

@app.route("/estudiantes",methods=["GET"])
def listar_estudiante():
    lista_estudiantes = estudiante_controller.index()
    return jsonify(lista_estudiantes)
@app.route("/estudiante",methods=["POST"])
def crear_estudiante():
    info_estudiante = request.get_json()
    estudiante_creado = estudiante_controller.create(info_estudiante)
    return jsonify(estudiante_creado)
@app.route("/estudiante/<string:id>",methods=["GET"])
def mostrar_estudiante(id):
    est = estudiante_controller.show(id)
    return jsonify(est)
@app.route("/estudiante/<string:id>",methods=["PUT"])
def actualizar_estudiante(id):
    inf_estudiante= request.get_json()
    estudiante_actualizado = estudiante_controller.update(id, info_estudiante)
    return jsonify(estudiante_actualizado)
@app.route("/estudiante/<string:id>",methods=["DELETE"])
def eliminar_estudiante(id):
    resp = estudiante_controller.delete(id)
    return jsonify(resp)





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

