from django.test import TestCase
from django.contrib.auth.models import User
from .forms import UserRegisterForm

class UserRegistrationTest(TestCase):
    def test_register_user_with_avatar(self):
        with open('path/to/avatar.jpg', 'rb') as avatar:
            form_data = {
                'username': 'testuser',
                'email': 'testuser@example.com',
                'password1': 'strongpassword123',
                'password2': 'strongpassword123',
            }
            files_data = {'avatar': avatar}
            form = UserRegisterForm(data=form_data, files=files_data)
            self.assertTrue(form.is_valid())
            form.save()
            user = User.objects.get(username='testuser')
            self.assertIsNotNone(user.profile.avatar)

    def test_register_user_without_avatar(self):
        form_data = {
            'username': 'testuser2',
            'email': 'testuser2@example.com',
            'password1': 'strongpassword123',
            'password2': 'strongpassword123',
        }
        form = UserRegisterForm(data=form_data)
        self.assertTrue(form.is_valid())
        form.save()
        user = User.objects.get(username='testuser2')
        self.assertIsNone(user.profile.avatar)
