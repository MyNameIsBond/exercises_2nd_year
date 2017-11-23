import unittest
from basic_1    import * 
from basic_2    import * 
from advanced_2 import * 
from advanced_1 import * 

class Test_week_1(unittest.TestCase):
    """Test for Week-1. Basic exersises"""

    def test_combine_str(self):
        result = combine_str('ok','not')
        self.assertEqual('onkot',result)


    def test_armstrong_num(self):
        result_c = armstrong_num(3)
        self.assertEqual(True,result_c)

        result_a = armstrong_num(4)
        self.assertEqual(True,result_a)

        result_b = armstrong_num(40)
        self.assertEqual(False,result_b)

    def test_larry(self):

        result_a = larry(2)
        self.assertEqual((0,8),result_a)

        result_c = larry(3)
        self.assertEqual((0,12),result_c)


    def test_factorial(self):

        result_a = factorial(6,9)
        self.assertEqual(True,result_a)

        result_b = factorial(6,27)
        self.assertEqual(False,result_b)

        result_c = factorial(20,10000)
        self.assertEqual(True,result_c)

        result_d = factorial(20,100000)
        self.assertEqual(False,result_d)


    def test_bonus_factorial(self):
        result_a = bonus_factorial(6,9)
        self.assertEqual(True,result_a)

        result_b = bonus_factorial(6,27)
        self.assertEqual(False,result_b)

        result_c = bonus_factorial(20,10000)
        self.assertEqual(True,result_c)

        result_d = bonus_factorial(20,100000)
        self.assertEqual(False,result_d)


if __name__ == '__main__':
    unittest.main()