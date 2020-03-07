from django.test import TestCase
from django.contrib.auth.models import User
from post.models import Post

# Create your tests here.

class PostTestCase(TestCase):
    def test_true_is_true(self):
        self.assertEqual(True, True)
    
    def test_post_pk_on_save(self):
        user = User()
        user.save()

        post = Post(title="Test Post", description="testing", author=user)
        post.save()

        # self.assertEqual(page.pk, 'my')

class PostListViewTestCases(TestCase):
    def test_multiple_posts(self):
        user = User.objects.create()

        Post.objects.create(title='test2', description='testing', author=user)
        Post.objects.create(title='test3', description='testing', author=user)

        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)

