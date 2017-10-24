
l1 = [3,1,9,2,1]
l2 = [2,1,2,1]

def polynomial(l1,l2):
	'''Adds two polynomials which are in a list form. '''
	solve = []
	if len(l1) > len(l2):
		l2 , l1 = l1 , l2  # swap if it is bigger. 
	for i in l2:
		solve.append(i)
	for k in range(len(l1)):
		solve[k] = solve[k] + l1[k] # adds the two numbers on the same list (solve)	
	print (solve)
		


polynomial(l1,l2)


class Polynomial:
	solve = []
	
	def __init__(self,l1,l2):
		self.l2 = l2
		self.l1 = l1

	def __str__(self):
		for i in self.solve:
			return i
	
	def __add__(self,l1,l2):

		'''Adds two polynomials which are in a list form. '''
		self.solve = []
		if len(self.l1) > len(self.l2):
			self.l2 , self.l1 = self.l1 , self.l2  # swap if it is bigger.
		for i in self.l2:
			self.solve.append(i)
		for k in range(len(self.l1)):
			self.solve[k] = self.solve[k] + self.l1[k] # adds the two numbers on the same list (solve)
		return self.solve
	def __mul__(self,l1,l2):
		pass


a = Polynomial(l1,l2)