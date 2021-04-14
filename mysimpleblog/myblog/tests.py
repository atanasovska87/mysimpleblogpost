from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from .views import AddPostView, HomeView


# Create your tests here.


class LandingPageTest(TestCase):

    def test_should_show_homepage(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')


class TestUrls(SimpleTestCase):

    def test_home_urls_resolves(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func.view_class, HomeView)

    def test_add_urls_resolves(self):
        url = reverse('add_post')
        self.assertEqual(resolve(url).func.view_class, AddPostView)
