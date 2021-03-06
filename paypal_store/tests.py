import unittest

from django.shortcuts import render_to_response
from django.test import Client


# check that users are redirected to paypal home page after completing a transaction
# check that users are redirected to paypal cancel page after cancelling a transaction
class SimpleTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_paypal_cancel(self):
        # Issue a GET request.
        response = self.client.get('/paypal/paypal_cancel.html/')

    def test_paypal_return(self):
        # Issue a GET request.
        response = self.client.get('/paypal/paypal_return.html/')

def test_home_page_status_code_is_ok(self):
    home_page = self.client.get('/')
    self.assertEquals(home_page.status_code, 200)


def test_check_paypal_return_is_correct(self):
        home_page = self.client.get('/')
        self.assertTemplateUsed(home_page, 'paypal/paypal_return.html')
        home_page_template_output = render_to_response('paypal/paypal_return.html').content
        self.assertEquals(home_page.content, home_page_template_output)


def test_check_paypal_cancel_is_correct(self):
        home_page = self.client.get('/')
        self.assertTemplateUsed(home_page, 'paypal/paypal_cancel.html')
        home_page_template_output = render_to_response('paypal/paypal_cancel.html').content
        self.assertEquals(home_page.content, home_page_template_output)


