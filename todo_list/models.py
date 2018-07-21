from .extensions import db


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    project = db.Column(db.String(100), nullable=False)
    done = db.Column(db.Boolean, default=True)