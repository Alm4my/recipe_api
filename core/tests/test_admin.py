from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            "admin@test.com",
            "password"
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            "normal_user@test.com",
            "password",
            first_name="Jane",
            last_name="Doe",
        )

    def test_users_listed(self):
        """Test that users are listed on user page."""
        # url for our list user page
        url = reverse('admin:core_user_changelist')
        resp = self.client.get(url)

        self.assertContains(resp, self.user.first_name)
        self.assertContains(resp, self.user.email)

    def test_user_change_page(self):
        """Check if the user edit works."""
        url = reverse('admin:core_user_change', args=[self.user.id])
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)

    def test_create_user_page(self):
        """Check if the create user page works."""
        url = reverse('admin:core_user_add')
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
