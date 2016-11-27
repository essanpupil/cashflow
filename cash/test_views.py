from django.test import TestCase, Client
from django.core.urlresolvers import reverse


class CashTestCase(TestCase):

    def setUp(self):
        self.client = Client()


class IndexTest(CashTestCase):

    def test_index(self):
        response = self.client.get(reverse('cash:index'))
        self.assertEqual(200, response.status_code)
        self.assertIn(b'<title>This is the cash application</title>', response.content)


class CashActivityTest(CashTestCase):

    def test_get_cash_activity(self):
        response = self.client.get(reverse('cash:new_activity'))
        self.assertEqual(200, response.status_code)


class ActivityListTest(CashTestCase):

    def test_get_activity_list(self):
        response = self.client.get(reverse('cash:activity_list'))
        self.assertEqual(200, response.status_code)
