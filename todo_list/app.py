import json
from . import app, db
from .models import Todo
from flask import render_template, request, jsonify
from flask_restful import reqparse, abort, Resource, Api


api = Api(app)


def abort_if_todo_doesnt_exist(todo_id):
    todo = Todo.query.get(todo_id)
    if not todo:
        abort(404, message="Todo {} doesn't exist".format(todo_id))


@app.route('/')
def index():
    return render_template('index.html')


class TodoViews(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('title', type=str, location='json')
    parser.add_argument('project', type=str, location='json')
    parser.add_argument('done', type=bool, location='json')

    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        todo = Todo.query.get(todo_id)
        return jsonify({
            'id': todo.id,
            'title': todo.title,
            'done': todo.done
            })


    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        todo = Todo.query.get(todo_id)
        todo = db.session.merge(todo)
        db.session.delete(todo)
        db.session.commit()
        return '', 204

    def put(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        todo = Todo.query.get(todo_id)
        done = json.loads(request.form['done'])
        todo.done = done
        db.session.merge(todo)
        db.session.commit()
        return jsonify(
            id=todo.id,
            title=todo.title,
            project=todo.project,
            done=todo.done
        )


class TodoList(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('title', type=str, location='json')
    parser.add_argument('project', type=str, location='json')
    parser.add_argument('done', type=bool, location='json')

    def get(self):
        _todos = Todo.query.all()
        todos = []
        [todos.append({
            'id': todo.id,
            'title': todo.title,
            'project': todo.project,
            'done': todo.done
        }) for todo in _todos]
        return jsonify(todos)


    def post(self):
        title = request.form['title']
        project = request.form['project']
        done = json.loads(request.form['done'])
        todo = Todo(title=title, project=project, done=done)
        db.session.add(todo)
        db.session.commit()
        return jsonify(
            id=todo.id,
            title=todo.title,
            project=todo.project,
            done=todo.done
        )


api.add_resource(TodoList, '/todos')
api.add_resource(TodoViews, '/todos/<string:todo_id>')


if __name__ == '__main__':
    app.run()