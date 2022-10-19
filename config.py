class Config(object):
    DEBUG = False
    TESTING = False

    SECRET_KEY = 'JDJDKEISLLLddldlmei'
    DB_NAME = 'production_db'
    DB_USERNAME = 'root'
    DB_PASSWORD= 'example'
    UPLOADS = '/home/username/app/static/images/uploads'
    SESSION_COOKIE_SECURE = True

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

    DB_NAME = 'development_db'
    DB_USERNAME = 'root'
    DB_PASSWORD= 'example'
    UPLOADS = '/home/username/projects/flask_test/app/static/images/uploads'
    SESSION_COOKIE_SECURE = True

class TestingConfig(Config):
    TESTING = True

    DB_NAME = 'development_db'
    DB_USERNAME = 'root'
    DB_PASSWORD= 'example'
    SESSION_COOKIE_SECURE = True

