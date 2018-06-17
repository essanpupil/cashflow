from datetime import datetime

from django.test import TestCase, Client
from django.urls import reverse

from . import models


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

    def test_post_cash_activity(self):
        form_data = {
            'description': 'Buy laptop',
            'value': 15000000,
            'activity_type': 'credit',
            'time': datetime.now()
        }
        response = self.client.post(reverse('cash:new_activity'), form_data)
        self.assertTrue(models.Activity.objects.get(description=form_data['description']))
        self.assertRedirects(response, expected_url=reverse('cash:activity_list'))


class ActivityListTest(CashTestCase):

    def test_get_activity_list(self):
        response = self.client.get(reverse('cash:activity_list'))
        self.assertEqual(200, response.status_code)

    def test_get_activity_list_with_value(self):
        models.Activity.objects.create(description='Buy notebook', value=5000000)
        response = self.client.get(reverse('cash:activity_list'))
        self.assertEqual(200, response.status_code)
        self.assertIn(b'Buy notebook', response.content)
