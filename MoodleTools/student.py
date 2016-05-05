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
        self._get_info_from_id(student_id)
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

    def _get_info_from_id(self, student_id):
        """
        Extract information from student id.
        Assign school, year, id information to class's field
        Id format:
        115010999
        1: 1 for undergraduate, 2 for graduate
        15: entering year
        010: 010 for SSE, 020 for SME, 030 for HSS (maybe)
        999: id in certain year and school
        Raises:
            LoginFailed if student id is in wrong format
        Args:
            student_id: student id in string
        Author:
            alesiong
        """
        if len(student_id) != 9 or not student_id.isdigit():
            # TODO: change LoginFailed to more specific error type
            raise LoginFailed
        year = student_id[0:3]
        school = student_id[3:6]
        id = student_id[6:9]
        # TODO: consider using returning value instead of setting fields directly
        if year[0] == '1':
            self._undergraduate = True
        elif year[1] == '2':
            self._undergraduate = False
        else:
            raise LoginFailed
        self._year = 2000 + int(year[1:])
        if school == '010':
            self._school = 1
        elif school == '020':
            self._school = 2
        elif school == '030':
            self._school = 3
        else:
            raise LoginFailed
        self._id = int(id)
