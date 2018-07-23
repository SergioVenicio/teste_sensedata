from . import app, db
from .models import Todo
from flask import render_template
from flask_restful import reqparse, abort, Resource, Api


api = Api(app)


def abort_if_todo_doesnt_exist(todo_id):
    todo = Todo.query.filter_by(id=todo_id)
    if not todo:
        abort(404, message="Todo {} doesn't exist".format(todo_id))


parser = reqparse.RequestParser()
parser.add_argument('task')


@app.route('/')
def index():
    return render_template('index.html')


class TodoViews(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return Todo.query.filter_by(id=todo_id)

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        todo = Todo.query.filter_by(id=todo_id)
        db.session.delete(todo)
        db.session.commit()
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        todo = Todo.query.filter_by(id=todo_id)
        todo.title = args['title']
        todo.project = args['project']
        todo.done = args['done']
        db.session.add(todo)
        db.session.commit()
        return todo, 201


class TodoList(Resource):
    def get(self):
        return Todo.query.all()

    def post(self):
        args = parser.parse_args()
        todo = Todo(args['title'], args['project'], args['done'])
        db.session.add(todo)
        db.session.commit()
        return todo, 201


api.add_resource(TodoList, '/todos')
api.add_resource(TodoViews, '/todos/<string:todo_id>')


if __name__ == '__main__':
    app.run(debug=True)