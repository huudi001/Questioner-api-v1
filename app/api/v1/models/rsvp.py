from ..utils import get_by_key

RSVP_LIST = []
class Rsvp():
    def put(self, rsvp_id, meetup_id, user_id, response):
        self.single_rsvp = {}

        rsvp= get_by_key('rsvp_id', rsvp_id, RSVP_LIST)
        if "message" not in rsvp:
            return {"message": "the rsvp id  you entered is being used for another rsvp"}



        self.single_rsvp['rsvp_id'] = rsvp_id
        self.single_rsvp['meetup_id'] = int(meetup_id)
        self.single_rsvp['user_id'] = int(user_id)
        self.single_rsvp['response'] = response

        RSVP_LIST.append(self.single_rsvp)

        return {"message": "Rsvp has been added successfully"}
