import os


basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    DEBUG = False
    TESTING = False
    TEMPLATE_AUTO_RELOAD = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(
        basedir, 'app.db'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    TEMPLATE_AUTO_RELOAD = True


class TestConfig(Config):
    DEBUG = True
    TESTING = False
    LIVESERVER_PORT = 5001
    SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(
        basedir, 'app_test.db'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = True


config = {
    'development': DevelopmentConfig,
    'test': TestConfig
}