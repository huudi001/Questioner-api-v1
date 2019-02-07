from flask import request, jsonify,  Blueprint
#from flask_jwt_extended import (JWTManager, jwt_required, get_jwt_claims)
import datetime
from ..models import rsvp
from ..models.rsvp import RSVP_LIST
from ..utils import get_by_key, _iterator


rsvps = Blueprint('rsvps', __name__, url_prefix='/api/v1')

db = rsvp.Rsvp()


@rsvps.route('/rsvps', methods=['POST'])
def post_rsvp():
    data = request.get_json()
    if not data:
        return jsonify({"message": "Fields cannot be empty"}), 400
    rsvp_id = len(RSVP_LIST) + 1





    question_id = data.get('question_id')
    meetup_id = data.get("meetup_id")
    user_id = data.get("user_id")
    response = data.get("response")



    rsvp_info = [question_id,meetup_id, user_id,response]

    info = _iterator(rsvp_info)
    if  info == False:
        return jsonify({"message": "Some required fields are missing!"}), 206


    response = jsonify(db.put(question_id, meetup_id, user_id, response))
    response.status_code = 200
    return response
