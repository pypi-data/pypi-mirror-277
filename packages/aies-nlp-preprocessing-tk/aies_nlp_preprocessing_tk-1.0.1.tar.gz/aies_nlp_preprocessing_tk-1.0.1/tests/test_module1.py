import unittest
from my_nlp_library.module1 import greet

class TestModule1(unittest.TestCase):

    def test_greet(self):
        self.assertEqual(greet("World"), "Hello, World!")

if __name__ == "__main__":
    unittest.main()