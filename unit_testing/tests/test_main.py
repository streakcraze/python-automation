import unittest
import json
from src.main import app, get_db

class TestMain(unittest.TestCase):
    def setUp(self):
        # Flask test client for simulating requests without running the server
        self.app = app.test_client()
        # Enable testing mode
        self.app.testing = True
        # Create the database table before each test
        with app.app_context():
            db = get_db()
            db.execute('CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY, name TEXT, value TEXT)')
            db.commit()

    def tearDown(self):
        # Drop the database table after each test
        with app.app_context():
            db = get_db()
            db.execute('DROP TABLE data')
            db.commit()

    def test_index(self):
        # Test the public route
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], "Welcome to the public page!")

    def test_get_data_unauthenticated(self):
        # Test the protected route without authentication
        response = self.app.get('/data')
        self.assertEqual(response.status_code, 401)

    def test_get_data_authenticated(self):
        # Test the protected route with authentication
        response = self.app.get('/data', headers={"Authorization": "Basic dXNlcjpwYXNzd29yZA=="})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [])

    def test_add_data_unauthenticated(self):
        # Test adding data to the protected route without authentication
        response = self.app.post('/data', data=json.dumps({"name": "test", "value": "123"}), content_type='application/json')
        self.assertEqual(response.status_code, 401)

    def test_add_data_authenticated(self):
        # Test adding data to the protected route with authentication
        response = self.app.post('/data', headers={"Authorization": "Basic dXNlcjpwYXNzd29yZA=="}, data=json.dumps({"name": "test", "value": "123"}), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['message'], "Data added successfully")

if __name__ == '__main__':
    unittest.main()
