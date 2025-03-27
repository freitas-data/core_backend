from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class UserModelTests(TestCase):

    def test_create_user(self):
        user = User.objects.create_user(
            email='teste@example.com',
            password='senhateste123'
        )
        self.assertEqual(user.email, 'teste@example.com')
        self.assertTrue(user.check_password('senhateste123'))
        self.assertFalse(user.is_staff)
        self.assertTrue(user.is_active)

    def test_create_superuser(self):
        admin = User.objects.create_superuser(
            email='admin@example.com',
            password='admin123'
        )
        self.assertTrue(admin.is_staff)
        self.assertTrue(admin.is_superuser)
