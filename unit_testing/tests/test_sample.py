import unittest
import json
from src.sample import app, get_db

class TestSample(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        with app.app_context():
            db = get_db()
            db.execute('CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY, name TEXT, value TEXT)')
            db.commit()

    def tearDown(self):
        with app.app_context():
            db = get_db()
            db.execute('DROP TABLE data')
            db.commit()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], "Welcome to the public page!")

    def test_get_data_unauthenticated(self):
        response = self.app.get('/data')
        self.assertEqual(response.status_code, 401)

    def test_get_data_authenticated(self):
        response = self.app.get('/data', headers={"Authorization": "Basic dXNlcjpwYXNzd29yZA=="})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [])

    def test_add_data_unauthenticated(self):
        response = self.app.post('/data', data=json.dumps({"name": "test", "value": "123"}), content_type='application/json')
        self.assertEqual(response.status_code, 401)

    def test_add_data_authenticated(self):
        response = self.app.post('/data', headers={"Authorization": "Basic dXNlcjpwYXNzd29yZA=="}, data=json.dumps({"name": "test", "value": "123"}), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['message'], "Data added successfully")

if __name__ == '__main__':
    unittest.main()