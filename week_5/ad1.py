import random as rnd



class Sum_check:

	def __init__(self,n,m):


		self.n = n
		self.m = m
		self.checking_list = []


	def create_matrix(self):
		''' creates the matrix according to the inputs. '''

		self.mat = [[rnd.randint(1,9) for i in range(self.m)] for i in range(self.m)] #matrix: n x m

		return self.mat

	def check_matrix(self):
		''' creating a list of diagonal inputs '''
		matrix = range(len(self.mat))

		for i in matrix:
			self.checking_list.append(self.mat[i][i])

	def check_sum(self):
		''' sort the list and sum the up 'n' numbers '''

		sorted_list = sorted(self.checking_list, reverse= True)
		if m > len(sorted_list):
			for i in range(m):
		else:

			print ('insert a smaller number.')





	def __str__(self):

		return ('\n'.join([' '.join(['{}'.format(number) for number in row]) for row in self.mat]))


if __name__ == '__main__':
	a = Sum_check(5,5)
	a.create_matrix()
	a.check_matrix()
	a.check_sum()
	print (a)
