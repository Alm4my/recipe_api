from django.contrib.auth.models import User
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email(self):
        """Test the creation of a new user with an email address."""
        email = "test@test.com"
        password = "NotS3cureP4ss_word"

        user: User = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        assert user.email == email
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the normalization of a new user's email address."""
        email = "test@THIS.SHOULD.BE.LOWERCASE.com"
        user: User = get_user_model().objects.create_user(
            email=email,
            password='test_pw'
        )
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test if creating a user with no email raises an error."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test_pw')

    def test_new_user_no_password(self):
        """Test if creating a user with no password raises an error."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user("test@test.test", None)

    def test_create_new_superuser(self):
        """Test creating a new superuser."""
        user = get_user_model().objects.create_superuser(
            'test@test.com', 'Test134'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
