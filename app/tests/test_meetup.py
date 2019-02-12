import json
import datetime
from base_test import BaseTestCase

class TestMeetups(BaseTestCase):






            response3 = self.client.post('/api/v1/meetups', data=json.dumps(dict()), content_type='application/json')
            response_data =  json.loads(response3.data)
            self.assertEqual("Fields cannot be empty", response_data["message"])
            self.assertEqual(response3.status_code, 400) 

    

