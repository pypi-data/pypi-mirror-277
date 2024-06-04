import unittest
from hello_meghana import hello

class TestHelloWorld(unittest.TestCase):

    def test_greet_user(self):
        self.assertEqual(hello(), "Hello, World!")
        

if __name__ == '_main_':
    unittest.main()