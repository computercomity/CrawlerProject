from bs4 import BeautifulSoup

from .config import MoodleConfig
from .error import *


class MoodleParser:
    """ The parser for moodle html codes

    Usage: Init this class with a html code of a moodle index page.
    Do some basic thing such as get info from html and return it to Student.
     Student class provide hte top api for user."""
    def __init__(self, html_page):
        self.soup = BeautifulSoup(html_page)
        self.moodle_conf = MoodleConfig()  # the variable defined in MoodleConfig() can be use here

    def get_ddl(self):
        pass

    # you can define method here
