from flask import Blueprint, jsonify, request
from courses.model.course_model import Course  # Importa el modelo de cursos

blueprint = Blueprint('course_controller', __name__)
courses=[]
# Endpoint para insertar cursos
@blueprint.route("/courses", methods=["POST"])
def insert_course():
    course_data = request.get_json()

    # Valida si el curso ya existe según su nombre
    existing_course = next((course for course in courses if course.name == course_data["name"]), None)

    if existing_course:
        return jsonify({"message": "El curso ya existe"}), 400

    # Crea un nuevo curso
    course = Course(
        id=len(courses) + 1,
        name=course_data["name"],
        description=course_data["description"]
    )

    # Agrega el nuevo curso a la lista de cursos
    courses.append(course)

    return jsonify(course)

# Endpoint para obtener un curso por ID
@blueprint.route("/courses/<course_id>", methods=["GET"])
def get_course(course_id):
    course = next((course for course in courses if course.id == int(course_id)), None)

    if course is None:
        return jsonify({"message": "Curso no encontrado"}), 404

    return jsonify(course)
