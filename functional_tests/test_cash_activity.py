from datetime import datetime
from selenium.webdriver.support.ui import Select

from django.utils import timezone

from functional_tests.base import BrowserTest


class CashActivityTest(BrowserTest):

    def test_enter_cash_activity_credit(self):
        # enter dashboard
        self.browser.get(self.live_server_url)
        self.assertEqual('Welcome to Cashflow', self.browser.title)
        cash_menu = self.browser.find_element_by_partial_link_text('Cash')
        cash_menu.click()

        # enter cash app index page
        self.assertEqual('This is the cash application', self.browser.title)
        new_cash_activity = self.browser.find_element_by_link_text('New cash activity')
        new_cash_activity.click()

        # enter input page  for cash activity
        self.assertEqual('Enter your cash activity here', self.browser.title)
        header_page = self.browser.find_element_by_tag_name('h3')
        self.assertEqual('Enter your cash activity here', header_page.text)

        # fill cash activity form & submit
        new_cash_activity_form = self.browser.find_element_by_id('cash_activity_form')
        activity_description = new_cash_activity_form.find_element_by_name('description')
        activity_description.send_keys('Buy laptop')
        activity_type = Select(new_cash_activity_form.find_element_by_name('activity_type'))
        activity_type.select_by_value('credit')
        activity_value = new_cash_activity_form.find_element_by_name('value')
        activity_value.send_keys('15000000')
        save_button = new_cash_activity_form.find_element_by_id('save_new_activity')
        save_button.click()

        # see the result in activity list page
        self.assertEqual('Cash activity list', self.browser.title)
        activity_list = self.browser.find_element_by_id('activity_list')
        self.assertIn('Buy laptop', activity_list.text)
