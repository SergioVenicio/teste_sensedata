import pytest
import unittest
from . import app, db, Todo


class TestModels(unittest.TestCase):
    def setUp(self):
        app.config.from_object('todo_list.config.TestConfig')
        db.create_all()
        return app

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_new_todo(self):
        todo = Todo(title='New Todo', project='Test')
        db.session.add(todo)
        db.session.commit()

        assert todo.title == 'New Todo'
        assert todo.project == 'Test'
        assert not todo.done


    def test_new_todo_complete(self):
        todo = Todo(title='New Todo', project='Test', done=True)
        db.session.add(todo)
        db.session.commit()

        assert todo.title == 'New Todo'
        assert todo.project == 'Test'
        assert todo.done


    def test_delete_todo(self):
        todo = Todo(title='New Todo', project='Test')
        db.session.add(todo)
        db.session.commit()

        todo = db.session.merge(todo)
        db.session.delete(todo)
        db.session.commit()

        assert Todo.query.count() == 0