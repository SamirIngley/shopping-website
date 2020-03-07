from django.test import RequestFactory, TestCase
from django.contrib.auth.models import User
from post.models import Post

# Create your tests here.

class UserTestCase(TestCase):
    def test_true_is_true(self):
        self.assertEqual(True, True)
    
    
class SearchFormTestCase(TestCase):
    def test_empty_get(self):
        response = self.client.get('/', HTTP_HOST='localhost')
        self.assertEqual(response.status_code, 200)