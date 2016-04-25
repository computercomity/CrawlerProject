from urllib import request, parse
import requests
import cookies
import json
import re

from MoodleTools.moodleParser import MoodleParser

from MoodleTools.config import StudentConfig
from MoodleTools.error import *


class Student:
    """ The basic class for student

    Usage: Init this class with the student id and password which you get from web or input.
    And then use method to do something. You can def your method by your own.
     If you do so, write down your name in the commend of your method """

    def __init__(self, student_id,
                 password):  # The password may need encryption
        self.__student_id = student_id
        self.__password = password
        self.config = StudentConfig()
        self.cookies = ''
        self.moodle_object = MoodleParser(self._get_index())

    def _get_index(self):
        """ login and get index response """
        username = self.__student_id
        data = {
            'username': username,
            'password': self.__password,
        }
        login_session = requests.Session()
        login_request = login_session.post(self.config.MOODLE_LOGIN_URL,
                                           data=data)
        self.cookies = login_request.cookies
        index_request = login_session.post(self.config.MOODLE_URL,
                                           cookies=self.cookies)
        return index_request.text

    def get_ddl(self):
        pass
        # write your function here, be care of your code style.
