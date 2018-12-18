from django.test import TestCase, Client

from post import defines, forms

class UrlsTest(TestCase):
    def setUP():
        self.client = Client()

    def test_expenses_page_status(self):
        response = self.client.get('/post/list/')
        self.assertEqual(response.status_code, defines.HTTP_200_OK)

    def test_category_page_status(self):
        response = self.client.get('/post/sc_list/')
        self.assertEqual(response.status_code, defines.HTTP_200_OK)

    def test_category_page_status(self):
        response = self.client.get('/post/tch_list/')
        self.assertEqual(response.status_code, defines.HTTP_302_FOUND)

class RedirectTest(TestCase):
    def setUP():
        self.client = Client()

    def test_tch_post_page_status(self):
        response = self.client.get('/post/tch_list/')
        self.assertRedirects(response, '/login/?next=/post/tch_list/',  status_code=302, target_status_code=200)



class FormsTest(TestCase):
    def test_comment_form(self):
        form_data = {'body': 'something'}
        form = forms.CommentForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertDictEqual(form.errors, {})
