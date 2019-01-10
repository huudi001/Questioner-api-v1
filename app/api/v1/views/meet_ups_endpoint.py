from flask import request, jsonify,  Blueprint
import datetime
from ..models import meetups
from ..models.meetups import MEETUPS_LIST
from ..utils import get_by_key, _iterator


meetup = Blueprint('meetup', __name__, url_prefix='/api/v1')

MeetUp = meetups.MeetUps()

@meetup.route('/meetups', methods=['POST'])
def post_meetup():
    data = request.get_json()
    if not data:
        return jsonify({"message": "Fields cannot be empty"}), 400
    meetup_id = len(MEETUPS_LIST) + 1
    now = datetime.datetime.now()
    created_on = now
    location = data.get("location")
    images= data.get("images")
    topic = data.get("topic")
    happening_on = now
    tags = data.get("tags")


    meetup_info = [created_on,location, images, topic, happening_on, tags]

    for i in meetup_info:
        if i not in meetup_info or i is None:
             return jsonify({"message": "Some required fields are missing!"}), 206
    response = jsonify(MeetUp.put(meetup_id, created_on, location, images, topic, happening_on, tags))
    response.status_code = 200
    return response
