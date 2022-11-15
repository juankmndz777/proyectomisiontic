from model.estudiante import Estudiante
class ControladorEstudiante:
    def __init__(self):
        print("creando el controlador de estudiantes")

    #listar
    def index(self):
        print("listar todos los estudiantes")
        estudiante1 = {
            "_id" : "abc100",
            "cedula": "12345",
            "nombre": "juan",
            "apellido": "mendez"
        }
        estudiante2 = {
            "_id": "abc101",
            "cedula": "12345",
            "nombre": "juanc",
            "apellido": "mendez a"
        }
        return [estudiante1, estudiante2]
    #crear
    def create(self,info_estudiante):
        print("crear un  estudiantes")
        nuevo_estudiante = Estudiante(info_estudiante)
        return nuevo_estudiante.__dict__
    #leer
    def show(self,id):
        print("mostrar un estudiantes")
        #buscamos en la base de datos y el resultado se guarda en estudiante2
        estudiante2 = {
            "_id": id,
            "cedula": "12345",
            "nombre": "juanc",
            "apellido": "mendez a"
        }
    #actualizae
    def update(self,id,info_estudiante):
        print("actualizando un estudiantes",id)
        estudiante_actualizado = Estudiante(info_estudiante)

    #delete
    def delete(self,id):
        print("eliminar un estudiantes con id ", id)
        return {"delected_count ": 1}
