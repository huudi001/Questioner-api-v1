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
