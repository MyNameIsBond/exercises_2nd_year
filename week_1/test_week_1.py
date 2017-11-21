import unittest
from week_1 import *

class Test_week_1(unittest.TestCase):
    """Test for Week-1. Basic exersises"""

    def test_combine_str(self):
        result = combine_str('ok','not')
        self.assertEqual('onkot',result)

    def test_armstrong_num(self):
        result_c = armstrong_num(3)
        self.assertEqual("3, Is an armstrong",result_c)
        result_a = armstrong_num(4)
        self.assertEqual("4, Is an armstrong",result_a)
        result_b = armstrong_num(40)
        self.assertEqual("40, It is not armstrong",result_b)

    def test_larry(self):

        result_a = larry(2)
        self.assertEqual((0,20),result_a)

        result_c = larry(30)
        self.assertEqual((6,177),result_c)



if __name__ == '__main__':
    unittest.main()