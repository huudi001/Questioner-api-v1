from flask import request, jsonify,  Blueprint
import datetime
from ..models import questions
from ..models.questions import QUESTIONS_LIST
from ..utils import get_by_key, _iterator


question = Blueprint('question', __name__, url_prefix='/api/v1')

Question = questions.Questions()

@question.route('/questions', methods=['POST'])
def post_question():
    data = request.get_json()
    if not data:
        return jsonify({"message": "Fields cannot be empty"}), 400
    question_id = len(QUESTIONS_LIST) + 1
    now = datetime.datetime.now()
    created_on = now
    created_by = data.get("created_by")
    meetup = data.get("meetup")
    title = data.get("title")
    body = data.get("body")
    votes = data.get("votes")


    question_info = [created_on,created_by, meetup, title, body, votes]

    for i in question_info:
        if i not in question_info or i is None:
             return jsonify({"message": "Some required fields are missing!"}), 206
    response = jsonify(Question.put(question_id, created_on, created_by, meetup, title, body, votes))
    response.status_code = 200
    return response
