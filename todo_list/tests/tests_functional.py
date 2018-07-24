import time
import pytest
import urllib3
from selenium import webdriver
from . import app, db, Todo
from flask_testing import LiveServerTestCase
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


class TestSitePages(LiveServerTestCase):
    def create_app(self):
        app.config.from_object('todo_list.config.TestConfig')
        db.create_all()
        return app

    def setUp(self):
        self._path = FirefoxBinary('/opt/firefox/firefox')
        self.browser = webdriver.Firefox(firefox_binary=self._path)
        self.base_url = self.get_server_url() + '/'
        self.http = urllib3.PoolManager()

    def tearDown(self):
        self.browser.quit()
        db.session.remove()
        db.drop_all()

    def test_home_page_title(self):
        self.browser.get(self.base_url)
        home_page_title = self.browser.find_element_by_class_name('navbar-brand').text
        self.assertEqual(home_page_title, 'Todo List')

    def test_home_page_status(self):
        response = self.http.request(url=self.base_url, method='GET')
        self.assertEqual(response.status, 200)

    def test_save_new_todo(self):
        self.browser.get(self.base_url)
        input_title = self.browser.find_element_by_id('title')
        input_project = self.browser.find_element_by_id('project')
        input_done = self.browser.find_element_by_id('done')
        input_save = self.browser.find_element_by_id('save')

        input_title.send_keys('New Todo')
        input_project.send_keys('Project for new todo')
        input_done.send_keys(Keys.ENTER)
        input_save.send_keys(Keys.ENTER)

        self.assertEqual(Todo.query.count(), 1)

    def test_list_todos_without_todos(self):
        self.browser.get(self.base_url)
        input_list = self.browser.find_element_by_id('list')
        input_list.send_keys(Keys.ENTER)
        self.browser.implicitly_wait(5)
        with pytest.raises(NoSuchElementException):
            self.browser.find_element_by_class_name('card-todo')


    def test_list_todos(self):
        new_todo = Todo(title='test', project='teste')
        db.session.add(new_todo)
        db.session.commit()
        self.browser.get(self.base_url)
        input_list = self.browser.find_element_by_id('list')
        input_list.send_keys(Keys.ENTER)
        self.browser.implicitly_wait(5)
        todos_title = self.browser.find_elements_by_class_name('card-text')
        todos_project = self.browser.find_elements_by_class_name('card-title')
        self.assertEqual(
            any(
                new_todo.project == _todo.text for _todo in todos_project
            ), True
        )
        self.assertEqual(
            any(
                new_todo.title == _todo.text for _todo in todos_title
            ), True
        )


    def test_delete_todo(self):
        new_todo = Todo(title='test', project='teste')
        db.session.add(new_todo)
        db.session.commit()
        self.browser.get(self.base_url)

        input_list = self.browser.find_element_by_id('list')
        inputs_delete = self.browser.find_elements_by_class_name('btn-danger')
        input_confirm = self.browser.find_element_by_id('confirm-button')
        input_list.send_keys(Keys.ENTER)
        for delete in inputs_delete:
            delete.click()
            input_confirm.click()

        new_todo = db.session.merge(new_todo)
        db.session.delete(new_todo)
        db.session.commit()
        self.assertEqual(Todo.query.count(), 0)