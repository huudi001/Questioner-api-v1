import datetime
from ..utils import get_by_key

MEETUPS_LIST = []


import datetime
class MeetUps():
    def put(self, meetup_id, created_on, location, images, topic, happening_on, tags):
        self.single_meetup = {}

        meetup = get_by_key('meetup_id', meetup_id,   MEETUPS_LIST)
        if "message" not in meetup:
            return {"message": "the meetup id  you entered is being used for another meetup"}





        #happening_on = str(dt.date(2019,6,12))
        created_on = datetime.datetime.now()










        self.single_meetup['meetup_id'] = meetup_id
        self.single_meetup['created_on'] = created_on
        self.single_meetup['location'] = location
        self.single_meetup['images'] = images
        self.single_meetup['topic'] = topic
        self.single_meetup['happening_on'] = happening_on
        self.single_meetup['tags'] = tags



        MEETUPS_LIST.append(self.single_meetup)

        return {"message": "MeetUp has been added successfully"}














    def get_upcoming(self,upcoming):
        upcoming = datetime.datetime.now().isoformat()

        meetup = [meetups for meetups in MEETUPS_LIST if meetups['happening_on'] > upcoming]






        return meetup



    def get_meetup_by_id(self, meetup_id):
        meetup = get_by_key('meetup_id', meetup_id, MEETUPS_LIST)
        if not meetup:
            return {"message:" "meetup does not exist"}
        return meetup
