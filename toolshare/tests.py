from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class HomePageViewTest(TestCase):

    def setup(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='admin@example.com',
            password='pedro6464'

        )

    def test_view_url_exists_by_name(self):
        response = self.client.get(reverse('home'))  # Or Location instead of name, change home to '/'
        self.assertEqual(response.status_code, 200)

    def test_view_url_exists_by_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_exists_by_location_2(self):
        response = self.client.get('tool/<int:pk>/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name_2(self):
        self.client.login(username='testuser', password='pedro6464')
        response = self.client.get(reverse('tool_create'))
        self.assertEqual(response.status_code, 200)

        self.client.logout()
        response = self.client.get(reverse('tool_create'))
        self.assertEqual(response.status_code, 302)  # Checks that a logged out person is forbidden



