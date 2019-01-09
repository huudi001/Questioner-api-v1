import json
import datetime
from base_test import BaseTestCase

class TestQuestions(BaseTestCase):

    def test_post_question(self):
        with self.client:
            response = self.client.post('/api/v1/questions', data=json.dumps(dict(question_id=1, created_by='khalid', meetup='upcoming', title='tech', body='technology', votes=200)), content_type='application/json')
            response_data = json.loads(response.data)
            self.assertEqual("Question has been added successfully", response_data["message"])
            self.assertEqual(response.status_code, 200)
