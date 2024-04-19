import unittest
from app import app


class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        app.config.from_object('config.TestingConfig')
        self.client = app.test_client()

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        response = self.client.post('/login', json={
            'username': 'admin',  # this must match the key in users_db
            'password': 'admin'  # this must match the password in users_db
        })
        self.assertEqual(response.status_code, 200)

    def login_client(self):
        return self.client.post('/login', json={
            'username': 'admin',
            'password': 'admin'
        }, follow_redirects=True)

    def test_show_data(self):
        login_response = self.login_client()  # Log in before trying to access protected route
        self.assertEqual(login_response.status_code, 200, "Login failed")
        response = self.client.get('/show-data')
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        response = self.client.get('/logout', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
