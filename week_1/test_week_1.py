import unittest
from week_1 import *


class Test_week_1(unittest.TestCase):
    """Test for Week-1. Basic exersises"""

    def test_combine_str(self):
        self.c = combine_str('ol','ok')
        self.assertEqual(self.c,'oolk')

    def test_armstrong_num(self):
        self.c = armstrong_num(5)
        self.assertEqual(self.c,)

    def test_factorial(self):
        self.c = factorial(2)
        self.assertEqual(3)

if __name__ == '__main__':
    unittest.main()