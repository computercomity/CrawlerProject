class Config:
    """ base configure for this package """
    MOODLE_LOGIN_URL = 'http://elearning.cuhk.edu.cn/login/index.php'


class MoodleConfig(Config):
    """ moodle config for parser """


class StudentConfig(Config):
    """ student config, for student management """


