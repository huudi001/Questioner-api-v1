import string
import datetime as dt
from flask import jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from ..utils import get_by_key, check_list

USERS_LIST = []


class Users():


    def put(self, user_id, firstname, lastname, othername, email, password, phoneNumber, username, isAdmin,registered):

        self.oneuser_dict = {}

        email_data = get_by_key("email", email, USERS_LIST)
        username_data = get_by_key("username", username, USERS_LIST)
        if "message" not in email_data:
            return {"message": "Email already in use,try a different one!"}
        if "message" not in username_data:
            return {"message": "Username already taken, try a different one"}

        user_id = len(USERS_LIST) + 1
        registered = dt.datetime.now()

        self.oneuser_dict["user_id"] = user_id
        self.oneuser_dict["firstname"] = firstname
        self.oneuser_dict["lastname"] = lastname
        self.oneuser_dict["othername"] = othername
        self.oneuser_dict["email"] = email
        pw_hash = generate_password_hash(password)
        self.oneuser_dict["password"] = pw_hash
        self.oneuser_dict["phoneNumber"] = phoneNumber
        self.oneuser_dict["username"] = username
        self.oneuser_dict["isAdmin"] = False
        self.oneuser_dict["registered"] = registered


        USERS_LIST.append(self.oneuser_dict)
        return {"message": "User with username {} added successfully".format(username)}

    def verify_password(self, username, password):

        user = get_by_key('username', username, USERS_LIST)
        if "message" not in user:
            result = check_password_hash(
                user['password'], password)
            if result is True:
                return "True"
            return {"message": "The password you entered is incorrect"}
        return user

    def get_user_by_username(self, username):
        result = get_by_key('username', username, USERS_LIST)
        return result

    def get_all_users(self):
        result = check_list(USERS_LIST)
        return result
