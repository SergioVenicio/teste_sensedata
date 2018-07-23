from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config.from_object('todo_list.config.DevelopmentConfig')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
