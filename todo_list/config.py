import os


basedir = os.path.abspath(os.path.dirname(__file__))

DABASE_URI = 'sqlite:////' + os.path.join(basedir, 'app.db')

class Config:
    DEBUG = True
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or DABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
