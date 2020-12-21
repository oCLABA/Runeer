import unittest
from main import *


class MyTestCase(unittest.TestCase):
    def test_usr_text(self):
        self.assertEqual(check_usr_text(60, 100), True)

    def test_usr_text_not_true(self):
        self.assertEqual(check_usr_text(10, 20), False)

    def test_check_background_is_true(self):
        self.assertEqual(check_background_position(0, 0), True)

    def test_check_background_not_true(self):
        self.assertEqual(check_background_position(10, 15), False)

if __name__ == '__main__':
    unittest.main()
