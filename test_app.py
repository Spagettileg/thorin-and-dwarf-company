import urllib
from flask import Flask
from flask_testing import TestCase


class test_home_directory_pages(TestCase):
    """
    Home page tested to return a positive 200 error code.
    """
    def test_home_page_is_rendered(self):
        url = self.client.get('/')
        self.assertEqual(url.status_code, 200)
        self.assertTemplateUsed(url, 'index.html')

    print("All the tests passed")
