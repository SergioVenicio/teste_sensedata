from todo_list.app import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)