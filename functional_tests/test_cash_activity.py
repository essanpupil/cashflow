from selenium.webdriver.support.ui import Select

from django.utils import timezone

from functional_tests.base import BrowserTest


class CashActivityTest(BrowserTest):

    def test_enter_cash_activity_credit(self):
        # enter dashboard
        self.browser.get(self.live_server_url)
        self.assertEqual('Welcome to Cashflow', self.browser.title)
        cash_menu = self.browser.find_element_by_link_text('Cash')
        cash_menu.click()

        # enter cash app index page
        self.assertEqual('This is the cash application', self.browser.title)
        new_cash_activity = self.browser.find_element_by_link_text('New cash ativity')
        new_cash_activity.click()

        # enter input page  for cash activity
        self.assertEqual('Enter your cash activity here', self.browser.title)
        header_page = self.browser.find_element_by_tag_name('h1')
        self.assertEqual('Enter your cash activity here', header_page.text)

        # fill cash activity form & submit
        new_cash_activity_form = self.browser.find_element_by_id('cash_activity_form')
        activity_description = new_cash_activity_form.find_element_by_name('description')
        activity_description.send_keys('Buy laptop')
        activity_time = new_cash_activity_form.find_element_by_name('time')
        activity_time.send_keys(str(timezone.localtime(timezone.now())))
        activity_type = Select(new_cash_activity_form.find_element_by_name('type'))
        activity_type.select_by_value('credit')
        activity_value = new_cash_activity_form.find_element_by_name('value')
        activity_value.send_keys('15000000')
        new_cash_activity_form.submit()

        # see the result in activity list
        self.assertEqual('Cash activity list', self.browser.title)
        activity_list = self.browser.find_element_by_id('activity_list')
        self.assertIn('Buy laptop', activity_list.text)
