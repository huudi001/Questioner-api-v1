import json
import datetime
from base_test import BaseTestCase

class TestMeetups(BaseTestCase):




    def test_post_meetup(self):
        with self.client:
            response = self.client.post('/api/v1/meetups', data=json.dumps(dict(meetup_id=100, location='mombasa',images='[image1, image2, image3]', topic='tech', tags='[data, sms, swahili pot]', happening_on='10/12/2018', created_on=str(datetime.datetime.now()) )), content_type='application/json')
            response_data = json.loads(response.data)
            self.assertEqual("MeetUp has been added successfully", response_data["message"])
            self.assertEqual(response.status_code, 201)
            response2 = self.client.post('/api/v1/meetups', data=json.dumps(dict(meetup_id=100, images='', topic='', tags='[data, sms, swahili pot]')), content_type='application/json')
            response_data = json.loads(response2.data)
            self.assertEqual("Some required fields are missing!", response_data["message"])
            self.assertEqual(response2.status_code, 206)

            response3 = self.client.post('/api/v1/meetups', data=json.dumps(dict()), content_type='application/json')
            response_data =  json.loads(response3.data)
            self.assertEqual("Fields cannot be empty", response_data["message"])
            self.assertEqual(response3.status_code, 400)

    def test_upcoming_meetings(self):
            self.client.post('/api/v1/meetups', data=json.dumps(dict(meetup_id=100, location='mombasa',images='[image1, image2, image3]', topic='tech', tags='[data, sms, swahili pot]', happening_on='10/12/2018', created_on=str(datetime.datetime.now()) )), content_type='application/json')
            result = self.client.get('/api/v1/meetups/upcoming')
            self.assertEqual(result.status_code, 200)
    def test_single_meetup(self):
        self.client.post('/api/v1/meetups', data=json.dumps(dict(meetup_id=1, location='mombasa',images='[image1, image2, image3]', topic='tech', tags='[data, sms, swahili pot]', happening_on='10/12/2018', created_on=str(datetime.datetime.now()) )), content_type='application/json')
        result = self.client.get('/api/v1/meetups/1')
        self.assertEqual(result.status_code, 200)
