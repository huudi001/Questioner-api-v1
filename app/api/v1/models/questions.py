from ..utils import get_by_key
import datetime
from ..models import meetups
from ..models.meetups  import  MEETUPS_LIST
from ..models import users
from ..models.users import USERS_LIST

QUESTIONS_LIST = []



class Questions():
    def put(self, question_id, created_on, created_by, meetup, title, body,votes):
        self.single_question = {}

        question = get_by_key('question_id', question_id, QUESTIONS_LIST)


        if "message" not in question:
            return {"message": "the question id  you entered is being used for another question"}


        created_on = datetime.datetime.now()







        self.single_question['question_id'] = question_id
        self.single_question['created_on'] = created_on
        self.single_question['created_by'] =int(created_by)
        self.single_question['meetup'] = int(meetup)
        self.single_question['title'] = title
        self.single_question['body'] = body
        self.single_question['votes'] = int(votes)



        QUESTIONS_LIST.append(self.single_question)
        return {"message": "Question has been added successfully"}







    def get_all_questions(self,meetup_id):


        question = [questions for questions in QUESTIONS_LIST if questions['meetup'] == meetup_id]
        if  not  question:
            return {"message": "question for this meetup does not exist"}
        return question








    def get_single_question(self, question_id):
        question = get_by_key('question_id', question_id, QUESTIONS_LIST)
        if not question:
            return {"message": "question does not exist"}
        return question
    def patch1(self,question_id):

        question = [questions for questions in QUESTIONS_LIST if questions['question_id'] == question_id]
        if not  question:
            return{"message": "question is not available"}
        question[0]['votes']+=1


        return {"message": "you upvoted thsi question"}


    def patch2(self,question_id):

        question= [questions for questions in QUESTIONS_LIST if questions['question_id'] == question_id]
        if  not question:
            return {"message":"question is not available"}
        question[0]['votes']-=1




        return {"message": "you downvoted this question"}
