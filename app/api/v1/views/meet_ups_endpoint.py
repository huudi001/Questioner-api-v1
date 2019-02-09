from flask import request, jsonify,  Blueprint
from flask_jwt_extended import (JWTManager, jwt_required, get_jwt_claims)
import datetime
from ..models import meetups
from ..models.meetups import MEETUPS_LIST
from ..utils import get_by_key, _iterator


meetup = Blueprint('meetup', __name__, url_prefix='/api/v1')

MeetUp = meetups.MeetUps()

@meetup.route('/meetups', methods=['POST'])
#@jwt_required
def post_meetup():
    data = request.get_json()
    if not data:
        return jsonify({"message": "Fields cannot be empty"}), 400
    meetup_id = len(MEETUPS_LIST) + 1






    location = data.get("location")
    images= data.get("images")
    topic = data.get("topic")
    tags = data.get("tags")
    happening_on = data.get('happening_on')
    created_on = data.get('created_on')




    meetup_info = [meetup_id, created_on,location, images, topic, happening_on, tags]

    info = _iterator(meetup_info)
    if  info == False:
        return jsonify({"message": "Some required fields are missing!"}), 206


    response = jsonify(MeetUp.put(meetup_id, created_on, location, images, topic, happening_on, tags))
    response.status_code = 201
    return response
@meetup.route('/meetups/<upcoming>', methods=['GET'])
#@jwt_required
def get_all(upcoming):
    response  = jsonify(MeetUp.get_upcoming(upcoming))
    response.status_code = 200
    return response

@meetup.route('/meetups/<int:meetup_id>', methods=['GET'])
#@jwt_required
def get_single_meetup(meetup_id):

    response = jsonify(MeetUp.get_meetup_by_id(meetup_id))
    response.status_code = 200
    return response
