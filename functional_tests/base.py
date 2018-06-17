from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.core.cache import cache


class BrowserTest(StaticLiveServerTestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920x1080")
        self.browser = WebDriver(chrome_options=chrome_options)
        self.browser.set_window_size(1024, 768)

    def tearDown(self):
        self.browser.quit()
        cache.clear()
