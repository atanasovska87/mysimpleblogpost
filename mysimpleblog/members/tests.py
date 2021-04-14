from django.contrib.auth import get_user_model, authenticate
from django.test import TestCase
from .models import Person
from django.contrib.auth.models import User
from django.urls import reverse


class RegisterPageTest(TestCase):

    def setUp(self):
        Person.objects.create(username='Tasha', first_name='Tasha', last_name='Atanasovska',
                              email='atanasovska87@hotmail.com', password_entry='roki12345',
                              password_confirm='roki12345')

    def test_person_creations(self):
        person = Person.objects.get(username='Tasha')
        self.assertTrue(isinstance(person, Person), 'Person is created')

    def test_verify_the_register_functionality(self):
        success_url = reverse('login')
        data = {
            'username': 'Tasha',
            'first_name': 'Tasha',
            'last_name': 'Atanasovska',
            'email': 'atanasovska87@hotmail.com',
            'password1': 'roki12345',
            'password2': 'roki12345'
        }
        url = reverse('register')  # HTTP URL
        response = self.client.post(path=url, data=data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(success_url, response.url)

    def test_verify_the_user_functionality(self):
        error_msg = 'This field is required.'
        data = {
            'username': '',
            'first_name': 'Tasha',
            'last_name': 'Atanasovska',
            'email': 'atanasovska87@hotmail.com',
            'password1': 'roki12345',
            'password2': 'roki12345'
        }
        url = reverse('register')  # HTTP URL
        response = self.client.post(path=url, data=data)
        errors = response.context_data.get('form').errors

        username_error = response.context_data['form'].errors.get('username').data[0].messages[0]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(error_msg, username_error)

    def test_verify_the_password_field(self):
        error_msg = 'This field is required.'
        data = {
            'username': '',
            'first_name': 'Tasha',
            'last_name': 'Atanasovska',
            'email': 'atanasovska87@hotmail.com',
            'password1': 'roki12345',
            'password2': 'roki12345'
        }
        url = reverse('register')  # HTTP URL
        response = self.client.post(path=url, data=data)
        errors = response.context_data.get('form').errors

        username_error = response.context_data['form'].errors.get('username').data[0].messages[0]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(error_msg, username_error)


class SigninTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='tasha', password='rokiitasha12345',
                                                         email='atanasovska87@hotmail.com')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        user = authenticate(username='tasha', password='rokiitasha12345')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username='sasha', password='rokiitasha12345')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_password(self):
        user = authenticate(username='tasha', password='roki')
        self.assertFalse(user is not None and user.is_authenticated)


class SimpleTestLogin(TestCase):

    def setUp(self):
        User = get_user_model()
        user = User.objects.create_user('tasha', 'atanasovska87@hotmail.com', 'roki12345')

    def test_secure_page(self):
        User = get_user_model()
        self.client.login(username='tasha', password='roki12345')
        url = reverse('login')
        response = self.client.get(path=url, follow=True)
        user = User.objects.get(username='tasha')


class TestUser(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='tasha', email='atanasovska87@hotmail.com', password='rokiitasha12345')

    def test_user_can_login(self):
        url_login = reverse('login')
        response_login = self.client.post(path=url_login, data={"username": "tasha", "password": "rokiitasha12345"})
        self.assertTrue(response_login.status_code, 200)
        url_home = reverse('home')
        self.assertTrue(self.client.get(url_home).status_code, 200)
