import unittest
from hello_world import greet_user

class TestHelloWorld(unittest.TestCase):

    def test_greet_user(self):
        self.assertEqual(greet_user("hi"), "Hello, World!")
        self.assertEqual(greet_user("HI"), "Hello, World!")
        self.assertEqual(greet_user("hello"), "Goodbye")
        self.assertEqual(greet_user("bye"), "Goodbye")

if __name__ == '__main__':
    unittest.main()

