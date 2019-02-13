from flask import request, jsonify,  Blueprint
from flask_jwt_extended import (JWTManager, jwt_required, get_jwt_claims)
import datetime
from ..models import meetups
from ..models.meetups import MEETUPS_LIST
from ..utils import get_by_key, _iterator


meetup = Blueprint('meetup', __name__, url_prefix='/api/v1')

MeetUp = meetups.MeetUps()
@meetup.route('/meetups/upcoming',methods=['GET'])
def get_all(upcoming):
    response  = jsonify(MeetUp.get_upcoming(upcoming))
    response.status_code = 200
    return response
