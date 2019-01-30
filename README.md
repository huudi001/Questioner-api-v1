
# Questioner-API

 Questioner is an application that helps meetup organizers prioritize questions to be answered.other users can vote on asked questions and they bubble up or down the log
### What you can Achieve
1. A user can add a meetup
2. A user can get all upcoming
3. A user can get a specific meetup
4. A user can post question to a specific meetup
5. users can up vote or down vote a question

### API Endpoints
| API Endpoint | Functionality |
| -----------  | ------------- |
| POST /api/v1/user/register |  Register a new user |
| POST /api/v1/user/login |  Logins in a user  |
| GET /api/v1/meetup/<upcoming >|  Fetch all upcoming meetups|
| POST /api/v1/meetups |  Create a single meetup into meetup list |
POST /api/v1/questons |  Create a single question into question list |
| GET /api/v1/meetups/<meetupId> |  Fetch a single meetup into meetups list |
| PATCH/api/v1/questiosn/<questionsId>/upvote |  upvote a specific question|
| PATCH /api/v1/questions/<questionsId> | down vote a specific question |




### How to run tests
This project has been implemented using unit tests. This is how you can test the endpoints:
* `git clone https://github.com/huudi001/Questioner-api-v1`
* `cd Questioner-api `
* Activate the virtual environment `virtualenv venv'
* Install all dependencies required `pip install -r requirements.txt`
* Now run the unittests `nosetests` or `nosetests app/tests/v1`
* Test API endpoints in postman
