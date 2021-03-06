from django.test import TestCase
from .models import Post
from users.models import Profile
from django.contrib.auth.models import User



class TestPost(TestCase):
    def setUp(self):
        self.user = User(username='kate')
        self.user.save()
        self.post_test = Post(id=1,caption='this is a sample test', image='default.png', user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.post_test, Post))

    def test_save_post(self):
        self.post_test.save_post()
        posts = Post.objects.all()
        self.assertTrue(len(posts) > 0)

    def test_delete_post(self):
        before = Profile.objects.all()
        self.post_test.delete_post()
        after = Profile.objects.all()
        self.assertTrue(len(before) == len(after))

