import json
import datetime
from base_test import  BaseTestCase
class Testauth(BaseTestCase):
    def test_registration(self):
        with self.client:
            response = self.client.post('/api/v1/register', data=json.dumps(dict(user_id=1,firstname='khalid',lastname='hai',othername='full',email='khalud604@gmail.com',password='Jinja2',confirm_password='Jinja2',phoneNumber='0706673533',username='hashi',isAdmin='False',registered=str(datetime.datetime.now()) )), content_type='application/json')
            response_data = json.loads(response.data)
            self.assertEqual("User added successfully",response_data["message"])
            self.assertEqual(response.status_code,201)

            response2 = self.client.post('/api/v1/register', data=json.dumps(dict(firstname='khal',lastname='hai',othername='gok',email='khal60@gmail.com',password='maneed',confirm_password='maneed',phoneNumber='',username='',isAdmin='True',registered=str(datetime.datetime.now()) )), content_type='application/json')
            response_data2 = json.loads(response2.data)
            self.assertEqual("Make sure all fields have been filled out",response_data2["message"])
            self.assertEqual(response2.status_code,206)

            response3 = self.client.post('/api/v1/register', data=json.dumps(dict( )), content_type='application/json')
            response_data3 = json.loads(response3.data)
            self.assertEqual("Fields cannot be empty",response_data3["message"])
            self.assertEqual(response3.status_code,400)

            response2 = self.client.post('/api/v1/register', data=json.dumps(dict(user_id=1,firstname='khalid',lastname='hai',othername='full',email='khalud604@gmail.com',password='Jinja2',confirm_password='Jinja2',phoneNumber='0706673533',username='hashi',isAdmin='False',registered=str(datetime.datetime.now()) )), content_type='application/json')
            response_data2 = json.loads(response2.data)
            self.assertEqual("Email already in use,try a different one!",response_data2["message"])

            response = self.client.post('/api/v1/register', data=json.dumps(dict(user_id=1,firstname='khalid',lastname='hai',othername='full',email='shirwa604@gmail.com',password='Jinja2',confirm_password='Jinja2',phoneNumber='0706673533',username='hashi',isAdmin='False',registered=str(datetime.datetime.now()) )), content_type='application/json')
            response_data = json.loads(response.data)

            self.assertEqual("Username already taken, try a different one",response_data["message"])

            response = self.client.post('/api/v1/register', data=json.dumps(dict(user_id=1,firstname='khalid',lastname='hai',othername='full',email='shirwa604@gmail.com',password='Jin',confirm_password='Jin',phoneNumber='0706673533',username='hashi',isAdmin='False',registered=str(datetime.datetime.now()) )), content_type='application/json')
            response_data = json.loads(response.data)
            self.assertEqual("The password is too short,minimum length is 4",response_data["message"])
            self.assertEqual(response.status_code,400)

            response = self.client.post('/api/v1/register', data=json.dumps(dict(user_id=1,firstname='khalid',lastname='hai',othername='full',email='shirwa604@gmail.com',password='Jinja2',confirm_password='maneed',phoneNumber='0706673533',username='hashi',isAdmin='False',registered=str(datetime.datetime.now()) )), content_type='application/json')
            response_data = json.loads(response.data)
            self.assertEqual("The passwords you entered don't match",response_data["message"])
            self.assertEqual(response.status_code,400)

            response = self.client.post('/api/v1/register', data=json.dumps(dict(user_id=1,firstname='khalid',lastname='hai',othername='full',email='shirwa604@gmail',password='Jinja2',confirm_password='Jinja2',phoneNumber='0706673533',username='hashi',isAdmin='False',registered=str(datetime.datetime.now()) )), content_type='application/json')
            response_data = json.loads(response.data)
            self.assertEqual("Enter a valid email address",response_data["message"])
            self.assertEqual(response.status_code,403)
    def test_login(self):
        with self.client:
            registered_user = self.client.post('/api/v1/register', data=json.dumps(dict(user_id=1,firstname='khalid',lastname='hai',othername='full',email='khalud604@gmail.com',password='maneed2',confirm_password='maneed2',phoneNumber='0706673533',username='has',isAdmin='False',registered=str(datetime.datetime.now()) )), content_type='application/json')
            response = self.client.post('/api/v1/login',data=json.dumps(dict(username='has',password='maneed2')),content_type='application/json')
            response_data = json.loads(response.data)



            self.assertEqual("Login successful!", response_data["message"])
            self.assertEqual(response.status_code, 200)
            response2 = self.client.post('/api/v1/login', data=json.dumps(dict()), content_type='application/json')
            response_data2 = json.loads(response2.data)
            self.assertEqual("Fields cannot be empty",response_data2["message"])
            self.assertEqual(response2.status_code,400)
            response3 = self.client.post('/api/v1/login', data=json.dumps(dict(username='khalid')), content_type='application/json')
            response_data3 = json.loads(response3.data)
            self.assertEqual("Username or password missing",response_data3["message"])
            self.assertEqual(response3.status_code,206)
    def test_user_logout(self):
        with self.client:
            # Register a user
            self.client.post(
                '/api/v1/register',
                data=json.dumps(dict(
                    firstname='mohamed',
                    lastname='hassan',
                    othername='amiin',
                    email='mary@gmail.com',
                    phoneNumber='09877444',
                    username='mary',
                    password='1234',
                    confirm_password='1234',
                    isAdmin='true',
                    registered=str(datetime.datetime.now())
                )),
                content_type='application/json'
            )
            response = self.client.post(
                '/api/v1/login',
                data=json.dumps(dict(
                    username='mary',
                    password='1234'

                )),
                content_type='application/json'
            )
            response_data = json.loads(response.data)
            token = response_data["token"]
            self.assertEqual("Login successful!", response_data["message"])
            self.assertEqual(response.status_code, 200)
            response2 = self.client.post(
                '/api/v1/logout', headers=dict(Authorization="Bearer " + token))
            response_data2 = json.loads(response2.data)
            self.assertEqual("Successfully logged out",
                             response_data2["message"])
            self.assertEqual(response.status_code, 200)

    def test_get_all_users(self):
        # Register a user
        self.client.post(
            '/api/v1/register',
            data=json.dumps(dict(
                firstname='mohamed',
                lastname='hassan',
                othername='amiin',
                email='mary@gmail.com',
                phoneNumber='09877444',
                username='mary',
                password='1234',
                confirm_password='1234',
                isAdmin='true',
                registered=str(datetime.datetime.now())
            )),
            content_type='application/json'
        )
        result = self.client.get('/api/v1/users')
        self.assertEqual(result.status_code, 200)

    def test_empty_users_list(self):
        result = self.client.get('/api/v1/users')
        result_data = json.loads(result.data)
        print(result_data)
        self.assertEqual("There are no records", result_data["message"])

    def test_get_user_by_username(self):
        with self.client:
            # REgister a user
            self.client.post(
                '/api/v1/register',
                data=json.dumps(dict(
                    firstname='mohamed',
                    lastname='hassan',
                    othername='amiin',
                    email='mary@gmail.com',
                    phoneNumber='09877444',
                    username='mary',
                    password='1234',
                    confirm_password='1234',
                    isAdmin='true',
                    registered=str(datetime.datetime.now())
                )),
                content_type='application/json'
            )
            result = self.client.get('/api/v1/users/mary')
            self.assertEqual(result.status_code, 200)
            # Test user by noexistent username
            result2 = self.client.get('/api/v1/users/amos')
            resp = json.loads(result2.data)
            self.assertEqual("username does not exist in our records", resp["message"])
