import unittest
import requests

class TestCalculatorApp(unittest.TestCase):

    BASE_URL = "http://localhost:5000"

    def test_add(self):
        response = requests.get(f"{self.BASE_URL}/?operation=add&num1=10&num2=5")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Result: 15.0", response.text)

    def test_subtract(self):
        response = requests.get(f"{self.BASE_URL}/?operation=subtract&num1=10&num2=5")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Result: 5.0", response.text)

    def test_multiply(self):
        response = requests.get(f"{self.BASE_URL}/?operation=multiply&num1=10&num2=5")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Result: 50.0", response.text)

    def test_divide(self):
        response = requests.get(f"{self.BASE_URL}/?operation=divide&num1=10&num2=5")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Result: 2.0", response.text)

    def test_divide_by_zero(self):
        response = requests.get(f"{self.BASE_URL}/?operation=divide&num1=10&num2=0")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Error: Division by zero", response.text)

    def test_invalid_input(self):
        response = requests.get(f"{self.BASE_URL}/?operation=add&num1=10&num2=abc")
        self.assertEqual(response.status_code, 400)
        self.assertIn("Error: Invalid input", response.text)

    def test_missing_parameters(self):
        response = requests.get(f"{self.BASE_URL}/?operation=add")
        self.assertEqual(response.status_code, 400)
        self.assertIn("Error: Missing parameters", response.text)

if __name__ == '__main__':
    unittest.main()
