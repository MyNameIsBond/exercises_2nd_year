import random as rnd
class Sum_check:

	def __init__(self,n,m):


		self.n = n
		self.m = m
		self.checking_list = []


	def create_matrix(self):
		''' creates the matrix according to the inputs. '''

		self.mat = [[rnd.randint(1,9) for i in range(self.n)] for i in range(self.n)] #matrix: n x n

		return self.mat

	def check_matrix(self):
		''' creating a list of diagonal inputs '''

		matrix = range(len(self.mat))

		for i in matrix:
			self.checking_list.append(self.mat[i][i])

	def check_sum(self):
		''' sorts the list and sums up 'n' numbers '''

		sum_up = 0
		sorted_list = sorted(self.checking_list,reverse=True)

		if self.m <= len(sorted_list):
			for i in range(self.m):
				print (sorted_list[i])
				sum_up += sorted_list[i]
			print (''.join(sorted_list[i]))

		else:
			print ('type a smaller number.')
			print ('the list is not that big.')
		print (sum_up)

	def __str__(self):
		''' print the matrix '''

		return ('\n'.join([' '.join(['{}'.format(number) for number in row]) for row in self.mat]))

if __name__ == '__main__':
	try:
		m = int(input('How many numbers you want to sum up?\t'))
		a = Sum_check(5,m)
		a.create_matrix()
		a.check_matrix()
		a.check_sum()
		print (a)
	except ValueError:
		print ('a number Should be given')
