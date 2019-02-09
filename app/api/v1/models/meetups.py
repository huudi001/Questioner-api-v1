from ..utils import get_by_key

MEETUPS_LIST = []


import datetime
class MeetUps():
    def put(self, meetup_id, created_on, location, images, topic, happening_on, tags):
        self.single_meetup = {}

        meetup = get_by_key('meetup_id', meetup_id,   MEETUPS_LIST)
        if "message" not in meetup:
            return {"message": "the meetup id  you entered is being used for another meetup"}


        created_on = str(datetime.datetime.now())
        self.single_question['meetup_id'] = meetup_id
        self.single_question['created_on'] = created_on
        self.single_question['location'] = location
        self.single_question['images'] = images
        self.single_question['topic'] = topic
        self.single_question['happening_on'] = happening_on
        self.single_question['tags'] = tags
        

        MEETUPS_LIST.append(self.single_meetup)

        return {"message": "MeetUp has been added successfully"}

    
    
