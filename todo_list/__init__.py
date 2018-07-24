from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, instance_relative_config=True)
app.config.from_object('todo_list.config.DevelopmentConfig')
db = SQLAlchemy(app)
db.create_all()
migrate = Migrate(app, db)
