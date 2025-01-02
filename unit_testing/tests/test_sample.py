import unittest
from src.sample import app

class TestSample(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_add(self):
        response = self.app.get('/add?a=1&b=2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], 3)

    def test_subtract(self):
        response = self.app.get('/subtract?a=2&b=1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], 1)

    def test_multiply(self):
        response = self.app.get('/multiply?a=2&b=3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], 6)

    def test_divide(self):
        response = self.app.get('/divide?a=6&b=3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], 2)
        response = self.app.get('/divide?a=1&b=0')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['error'], "Cannot divide by zero")

if __name__ == '__main__':
    unittest.main()