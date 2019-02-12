from ..utils import get_by_key

MEETUPS_LIST = []


import datetime
class MeetUps()
    def get_upcoming(self,upcoming):
        upcoming = datetime.datetime.now().isoformat()

        meetup = [meetups for meetups in MEETUPS_LIST if meetups['happening_on'] > upcoming]
        return meetup
