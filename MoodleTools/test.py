from MoodleTools.student import Student

from getpass import getpass

if __name__ == '__main__':
    # This is for function testing
    user_id = input("Please input your student id:")
    password = getpass("Please input your password:")
    student = Student(user_id, password)
    print(student.get_ddl())