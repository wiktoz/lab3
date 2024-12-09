from flask import request, Response, jsonify, Blueprint
from models.student import Student

student_bp = Blueprint("student_bp", __name__, url_prefix="/api/student")



@student_bp.route("/max-lessons", methods=["GET"])
def get_student_max_lessons():
    groups = Student.query.all()
    groups_list = [group.to_dict() for group in groups]
    
    return jsonify(groups_list), 200