import unittest
from basic_1     import *
from basic_2     import *
from basic_2_2nd import *




class Test_Week_3(unittest.TestCase):
    '''Test week 3 '''
    def test_prints_backwards(self):
        func = prints_backwards(1,'backwards')
        solution = 'sdrawkcab'
        self.assertEqual(solution,func)

    def test_linear_recursive(self):
        pass

if __name__ == '__main__':
	unittest.main()

    

