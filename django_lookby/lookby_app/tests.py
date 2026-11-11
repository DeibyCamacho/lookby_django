from django.test import SimpleTestCase
from django.urls import reverse


class LookByRoutesTests(SimpleTestCase):
    def test_home_route_exists(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_login_route_exists(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_client_dashboard_route_exists(self):
        response = self.client.get(reverse('client_dashboard'))
        self.assertEqual(response.status_code, 200)
