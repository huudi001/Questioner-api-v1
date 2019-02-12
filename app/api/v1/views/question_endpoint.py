from flask import request, jsonify,  Blueprint
#from flask_jwt_extended import (JWTManager, jwt_required, get_jwt_claims)
import datetime
from ..models import questions, meetups, users
from ..models.questions import QUESTIONS_LIST
from ..utils import get_by_key, _iterator, check_list


question = Blueprint('question', __name__, url_prefix='/api/v1')

Question = questions.Questions()

@question.route('/questions', methods=['POST'])
#@jwt_required
def post_question():
    data = request.get_json()
    if not data:
        return jsonify({"message": "Fields cannot be empty"}), 400
    question_id = len(QUESTIONS_LIST) + 1


    created_on = data.get("created_on")
    title = data.get("title")
    body = data.get("body")
    votes = data.get("votes")
    created_by = data.get("created_by")
    meetup = data.get("meetup")


    question_info = [question_id,created_on,created_by, meetup, body, title, votes]

    getter = _iterator(question_info)
    if getter == False:
        return jsonify({"message": "Some required fields are missing!"}), 206
    response = jsonify(Question.put(question_id, created_on, created_by, meetup, title, body, votes))
    response.status_code = 201
    return response
