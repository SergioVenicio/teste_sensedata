import urllib3
from todo_list.app import app
from selenium import webdriver
from flask_testing import LiveServerTestCase
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


class TestSitePages(LiveServerTestCase):
    def create_app(self):
        app.config['LIVESERVER_PORT'] = 5000
        return app

    def setUp(self):
        self._path = FirefoxBinary('/opt/firefox/firefox')
        self.browser = webdriver.Firefox(firefox_binary=self._path)
        self.base_url = self.get_server_url() + '/'
        print(self.base_url)
        self.http = urllib3.PoolManager()

    def tearDown(self):
        self.browser.quit()

    def test_home_page_title(self):
        self.browser.get(self.base_url)
        home_page_title = self.browser.find_element_by_class_name('navbar-brand').text
        self.assertEqual(home_page_title, 'Todo List')

    def test_home_page_status(self):
        response = self.http.request(url=self.base_url, method='GET')
        self.assertEqual(response.status, 200)