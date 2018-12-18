from django.test import TestCase, Client

from main_page import defines

class UrlsTest(TestCase):
    def setUP():
        self.client = Client()

    def test_home_page_status(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, defines.HTTP_200_OK)


class ContentsTest(TestCase):
    def setUP():
        self.client = Client()

    def test_home_page_status(self):
        response = self.client.get('')
        self.assertContains(response, 'Main Page')

