import os


basedir = os.path.abspath(os.path.dirname(__file__))

DABASE_URI = 'sqlite:////' + os.path.join(basedir, 'app.db')

class Config:
    DEBUG = False
    TESTING = False
    TEMPLATE_AUTO_RELOAD = False
    SQLALCHEMY_DATABASE_URI = DABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    TEMPLATE_AUTO_RELOAD = True


class TestConfig(Config):
    DEBUG = True
    TESTING = False
    DABASE_URI = 'sqlite:////' + os.path.join(basedir, 'app_test.db')
    SQLALCHEMY_DATABASE_URI = DABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = True


config = {
    'development': DevelopmentConfig,
    'test': TestConfig
}