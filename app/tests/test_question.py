import json
import datetime
from base_test import BaseTestCase

class TestQuestions(BaseTestCase):
    def test_post_question(self):
        with self.client:
            response2 = self.client.post('/api/v1/questions', data=json.dumps(dict(created_on=str(datetime.datetime.now()),question_id=1, created_by=1, meetup=2, title='tech', body='technology', votes=2)), content_type='application/json')
            response_data = json.loads(response2.data)
            self.assertEqual("Question has been added successfully", response_data["message"])
            self.assertEqual(response2.status_code, 201)

            response = self.client.post('/api/v1/questions', data=json.dumps(dict(created_on=str(datetime.datetime.now()), created_by=1, question_id=1,meetup=2, title='', body='', votes=2)), content_type='application/json')
            response_data = json.loads(response.data)
            self.assertEqual("Some required fields are missing!", response_data["message"])
            self.assertEqual(response.status_code, 206)
            empty_response = self.client.post('/api/v1/questions', data=json.dumps(dict()),content_type='application/json')
            response_data = json.loads(empty_response.data)
            self.assertEqual("Fields cannot be empty",response_data["message"])
            self.assertEqual(empty_response.status_code, 400)
    def test_get_questions_by_id(self):
        self.client.post('/api/v1/meetups', data=json.dumps(dict(meetup_id=1, location='mombasa',images='[image1, image2, image3]', topic='tech', tags='[data, sms, swahili pot]', happening_on='10/12/2018', created_on=str(datetime.datetime.now()) )), content_type='application/json')
        self.client.post('/api/v1/questions', data=json.dumps(dict(created_on=str(datetime.datetime.now()),question_id=1, created_by=1, meetup=2, title='tech', body='technology', votes=2)), content_type='application/json')
        result = self.client.get('/api/v1/questions/1')
        self.assertEqual(result.status_code,200)
    def test_upvote_quetion(self):
        self.client.post('/api/v1/questions', data=json.dumps(dict(created_on=str(datetime.datetime.now()),question_id=1, created_by=1, meetup=2, title='tech', body='technology', votes=2)), content_type='application/json')
        result = self.client.patch('/api/v1/questions/1/upvote')
        self.assertEqual(result.status_code,200)
    def test_downvote_quetion(self):
          self.client.post('/api/v1/questions', data=json.dumps(dict(created_on=str(datetime.datetime.now()),question_id=1, created_by=1, meetup=2, title='tech', body='technology', votes=2)), content_type='application/json')
          result = self.client.patch('/api/v1/questions/1/downvote')
          self.assertEqual(result.status_code,200)
