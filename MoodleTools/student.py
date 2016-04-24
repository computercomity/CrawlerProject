from urllib import request, parse
import requests
import json

from .moodleParser import MoodleParser
from .config import StudentConfig
from .error import *

class Student:
    """ The basic class for student

    Usage: Init this class with the student id and password which you get from web or input.
    And then use method to do something. You can def your method by your own.
     If you do so, write down your name in the commend of your method """
    def __init__(self, student_id, password):  # The password may need encryption
        self.__student_id = student_id
        self.__password = password
        self.config = StudentConfig()
        self.moodle_object = MoodleParser(self.get_index())

    def get_index(self):
        """ login and get index response """
        pass

    # write your function here, be care of your code style.
