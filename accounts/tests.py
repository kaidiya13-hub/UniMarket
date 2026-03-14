from django.test import TestCase
from django.contrib.auth.models import User

class UserTest(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(username='teststudent', email='test@glasgow.ac.uk', password='password123')
        self.assertEqual(user.username, 'teststudent')