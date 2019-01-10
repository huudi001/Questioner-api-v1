import json
import datetime
from base_test import BaseTestCase

class TestMeetups(BaseTestCase):

    def test_post_meetup(self):
        with self.client:
            response = self.client.post('/api/v1/meetups', data=json.dumps(dict(meetup_id=1, location='mombasa',images='['image1', 'image2', 'image3']',topic='tech', tags='['data', 'sms', 'swahili pot']',)), content_type='application/json')
            response_data = json.loads(response.data)
            self.assertEqual("MeetUp has been added successfully", response_data["message"])
self.assertEqual(response.status_code, 200)
