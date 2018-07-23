from . import app
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy(app)
migrate = Migrate(app, db)