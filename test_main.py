# test_main.py
import unittest
from main import hello_world, greet_person

class TestHelloWorld(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world(), "Hello from Git!")

    def test_greet_person(name):
        name.assertEqual(greet_person(name), f"Hello, {name}!")

if __name__ == '__main__':
    unittest.main()