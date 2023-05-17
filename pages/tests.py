from django.test import TestCase
from django.shortcuts import reverse


class PageViewTest(TestCase):
    def test_home_page_view_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_view_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Home Page')
        self.assertTemplateUsed(response, 'home.html')

    def test_about_page_view_url(self):
        response = self.client.get('/aboutus')
        self.assertEqual(response.status_code, 200)

    def test_about_page_view_name(self):
        response = self.client.get(reverse('aboutus'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'AboutUs Page')
        self.assertTemplateUsed(response, 'pages/aboutus.html')
