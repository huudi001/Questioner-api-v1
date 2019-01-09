from ..utils import get_by_key

QUESTIONS_LIST = []


import datetime
class Questions():
    def put(self, question_id, created_on, created_by, meetup, title, body,votes):
        self.single_question = {}

        question = get_by_key('question_id', question_id, QUESTIONS_LIST)
        if "message" not in question:
            return {"message": "the question id  you entered is being used for another question"}



        self.single_question['question_id'] = question_id
        self.single_question['created_on'] = created_on
        self.single_question['created_by'] = created_by
        self.single_question['meetup'] = meetup
        self.single_question['title'] = title
        self.single_question['body'] = body
        self.single_question['votes'] = votes

        QUESTIONS_LIST.append(self.single_question)

        return {"message": "Question has been added successfully"}
