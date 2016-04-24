from .student import Student
from .error import *

from getpass import getpass

if __name__ == '__main__':
    # This is for function testing
    user_id = input("Please input your student id")
    password = getpass("Please input your password")
    student = Student(user_id, password)
    try:
        student.get_index()
    except LoginFailed as e:
        print("Wrong id or password!")
    except NetworkError as e:
        print("Cannot connect to moodle!")
