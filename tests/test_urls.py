from django.test import SimpleTestCase
from django.urls import resolve, reverse
from webpages.views import home, user_profile


class TestUrls(SimpleTestCase):
    def test_home_url(self):
        url = reverse("home")
        self.assertEqual(resolve(url).func, home)

    def test_users_url(self):
        url = reverse("users")
        self.assertEqual(resolve(url).url_name, "users")

    def test_user_profile_url(self):
        url = reverse("user", args=[40])
        self.assertEqual(resolve(url).func, user_profile)
