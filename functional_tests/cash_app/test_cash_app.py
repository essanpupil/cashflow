from functional_tests.test import BrowserTest


class CashTest(BrowserTest):

    def test_open_homepage(self):
        self.browser.get(self.live_server_url)
        self.assertEqual("Welcome to cashflow", self.browser.title)
