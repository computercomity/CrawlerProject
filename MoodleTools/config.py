# config file


class Config:
    """ base configure for this package

    basic configuration for this project."""
    MOODLE_LOGIN_URL = 'http://elearning.cuhk.edu.cn/login/index.php'
    MOODLE_URL = 'http://elearning.cuhk.edu.cn/'


class MoodleConfig(Config):
    """ moodle config for parser

    tag name settings, all the regulation should be set here.
    no need to use self domain."""


class StudentConfig(Config):
    """ student config, for student management

    top configuration for this feature."""


class DBConfig(Config):
    """ Database configuration(if there has any database we need) """


