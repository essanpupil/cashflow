from selenium import webdriver

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.core.cache import cache


class BrowserTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.PhantomJS()
        self.browser.set_window_size(1024, 768)

    def tearDown(self):
        self.browser.quit()
        cache.clear()

    def test_homepage(self):
        self.browser.get(self.live_server_url)
        self.assertEqual('Welcome to Cashflow', self.browser.title)

    def test_enter_cash_menu(self):
        self.browser.get(self.live_server_url)
        self.assertEqual('Welcome to Cashflow', self.browser.title)
        cash_menu = self.browser.find_element_by_link_text('Cash')
        cash_menu.click()
        self.assertEqual('This is the cash application', self.browser.title)
