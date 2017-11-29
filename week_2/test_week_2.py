from  basic_1 import *
from advanced_1 import *
import unittest


class test_Polynomial(unittest.TestCase):
	"""testing 2nd week."""
	def test_Polynomial(self):
		self.l1 = [3,1,9]
		self.l2 = [2,1,2,1]

		solution_add = [2,4,3,10]
		solution_mul = [6,5,25,14,19,9]
		instance = Polynomial(self.l1,self.l2)

		self.assertEqual(solution_add,instance.__add__())
		self.assertEqual(solution_mul,instance.__mul__())

	def test_eight_queens(self):
		solution_list = [(0, 0), (1, 2), (2, 4), (3, 1),(4,3)]
		instance = Eight_Queens(8)
		instance.solve()

		self.assertEqual(solution_list,instance.solution())



if __name__ == '__main__':
	unittest.main()


