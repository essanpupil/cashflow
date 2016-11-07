from selenium import webdriver

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.core.cache import cache


class BrowserTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.set_window_size(1024, 768)

    def tearDown(self):
        self.browser.quit()
        cache.clear()

    def test_open_homepage(self):
        self.browser.get(self.live_server_url)
        self.assertEqual("Welcome to cashflow", self.browser.title)
