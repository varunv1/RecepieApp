from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        '''Test creating a new user successful'''
        email = 'abcxyz@abv.com'
        password = 'asfgvegrf'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_user_email_normalized(self):
        '''To test if the new email is normalized'''

        email = "thisismyemail@GMAIL.com"
        user = get_user_model().objects.create_user(email, 'afvbdfs')
        self.assertEqual(user.email, email.lower())

    def test_user_email_invalid(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'sfghfds')

    def test_create_super_user(self):
        user = get_user_model().objects.create_superuser(
            'test@test.com', 'egdfgbd'
        )
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)


