import unittest
from app import create_app, mongo
from flask import Flask, session
from flask_pymongo import PyMongo
from flask_mail import Mail
from app.routes import register_routes

class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        """Set up the test client and the application context."""
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['MONGO_URI'] = 'mongodb://localhost:27017/test_database'
        self.app.config['MAIL_DEFAULT_SENDER'] = 'test@example.com'

        # Set up the test client
        self.client = self.app.test_client()
        
        # Prepare the database
        with self.app.app_context():
            # Insert test user into the test database
            mongo.db['users'].insert_one({
                'username': 'testuser',
                'password': 'hashedpassword'
            }) 

    def tearDown(self):
        """Clean up after each test."""
        
        with self.app.app_context():
            mongo.db.users.delete_many({})
            mongo.cx.close()

    def test_index_post_success(self):
        """Test successful form submission on the index route."""
        response = self.client.post('/index', data={
            'name': 'John Doe',
            'email': 'john@example.com',
            'message': 'Hello!'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'success', response.data)

    def test_index_post_missing_fields(self):
        """Test form submission with missing fields on the index route."""
        response = self.client.post('/index', data={
            'name': '',
            'email': 'john@example.com',
            'message': 'Hello!'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'All fields are required', response.data)

    def test_login_success(self):
        """Test successful login."""
        self.mongo.db.users.insert_one({
            'username': 'existing_user',
            'password': b'$2b$12$KIXQ1Z1Q1Z1Q1Z1Q1Z1Q1u'
        })
        response = self.client.post('/login', data={
            'username': 'existing_user',
            'passwrd': 'correct_password'
        })
        with self.app.app_context():
            self.assertIn('username', session)
        self.assertEqual(response.status_code, 302)

    def test_login_missing_fields(self):
        """Test login with missing fields."""
        response = self.client.post('/login', data={
            'username': '',
            'passwrd': ''
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Username and password are required', response.data)

    def test_signup_success(self):
        """Test successful signup."""
        response = self.client.post('/signup', data={
            'fullname': 'Jane Doe',
            'username': 'new_user',
            'email': 'jane@example.com',
            'passwrd': 'new_password'
        })
        self.assertEqual(response.status_code, 302)

    def test_signup_missing_fields(self):
        """Test signup with missing fields."""
        response = self.client.post('/signup', data={
            'fullname': '',
            'username': 'new_user',
            'email': 'jane@example.com',
            'passwrd': 'new_password'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'All fields are required', response.data)

    def test_choice_access_when_logged_in(self):
        """Test access to choice page when logged in."""
        with self.app.test_request_context():
            with self.app.test_client() as client:
                with client.session_transaction() as sess:
                    sess['username'] = 'existing_user'
                response = client.get('/choice')
                self.assertEqual(response.status_code, 200)
                self.assertIn(b'Choice', response.data)

    def test_choice_access_when_not_logged_in(self):
        """Test access to choice page when not logged in."""
        response = self.client.get('/choice')
        self.assertEqual(response.status_code, 302)

if __name__ == '__main__':
    unittest.main()
