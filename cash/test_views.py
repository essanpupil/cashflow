from django.test import TestCase, Client
from django.core.urlresolvers import reverse


class IndexTest(TestCase):

    def test_index(self):
        client = Client()
        response = client.get(reverse('cash:index'))
        self.assertEqual(200, response.status_code)
        self.assertIn(b'<title>This is the cash application</title>', response.content)


class CashActivityTest(TestCase):

    def test_get_cash_activity(self):
        client = Client()
        response = client.get(reverse('cash:new_activity'))
        self.assertEqual(200, response.status_code)
