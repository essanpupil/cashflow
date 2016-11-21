from django.test import TestCase, Client
from django.core.urlresolvers import reverse


class CashFlowTest(TestCase):

    def test_homepage(self):
        client = Client()
        response = client.get(reverse('home'))
        self.assertEqual(200, response.status_code)
