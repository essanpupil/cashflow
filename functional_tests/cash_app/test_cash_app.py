from functional_tests.test import BrowserTest


class CashTest(BrowserTest):

    def test_open_homepage(self):
        self.browser.get(self.live_server_url)
        self.assertEqual("Welcome to cashflow", self.browser.title)

    def test_cashflow_menu(self):
        self.browser.get(self.live_server_url)
        cashflow_menu = self.browser.find_element_by_id("cashflow_menu")
        cashflow_menu.click()
        self.assertEqual("Cashflow page", self.browser.title)
