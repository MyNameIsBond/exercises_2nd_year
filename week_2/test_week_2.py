from  week_2 import *
import unittest


class Test_week_2(unittest.TestCase):
	"""testing 2nd week."""
	def test_polynomial(self):
		self.l1 = [3,1,9]
		self.l2 = [2,1,2,1]
		solution = [2,4,3,10]
		s = ppolynomial(self.l1,self.l2)
		self.assertEqual(solution,s)

	def test_Polynomial(self):
		pass




if __name__ == '__name__':
	unittest.main()

