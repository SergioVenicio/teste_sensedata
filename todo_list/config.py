import os


basedir = os.path.abspath(os.path.dirname(__file__))

DABASE_URI = 'sqlite:////' + os.path.join(basedir, 'app.db')

class Config:
    DEBUG = False
    TESTING = False
    TEMPLATE_AUTO_RELOAD = False
    SQLALCHEMY_DATABASE_URI = DABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopmentConfig(Config):
    DEBUG = True
    TEMPLATE_AUTO_RELOAD = True


config = {
    'development': DevelopmentConfig
}