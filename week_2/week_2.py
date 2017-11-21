
l1 = [3,1,9]
l2 = [2,1,2,1]

def polynomial(l1,l2):
	'''Adds two polynomials which are in a list form. '''
	solve = []
	l1 = list(reversed(l1)) 
	l2 = list(reversed(l2)) 
	
	if len(l1) > len(l2):
		l2 , l1 = l1 , l2  # swap if it is bigger.

	for i in l2:
		solve.append(i)

	for k in range(len(l1)):
		solve[k] = solve[k] + l1[k] # adds the two numbers on the same list (solve)
		
	solve = list(reversed(solve))
	print (solve)

# polynomial(l1,l2)
'''
b) Given the following pseudocode, first understand how it works, 
then implement the code for multiplying
the two polynomials in the programming language of your choice.

• Create a result array Res[], of size m + n + 1, 
where m is the degree of the first polynomial and n is
the degree of the second polynomial

• Initialise all the array elements as 0

• For each element of P1 (corresponding to index i) and each element of P2 
(corresponding to indexj), perform the following operation

res[i+j] = res[i+j] + P1[i]*P2[j], where i is the index for P1 and j is the index for P2.

Hint: Use a nester FOR loop to traverse both arrays.

• Return res

'''
import numpy as np
l1 = [3,1,9]
l2 = [2,1,2,1]

def mult_poly(l2,l1):
	# n = [i for i in l2]
	# m = [i for i in l1]
	res = np.array([[i*k for i in l1],[k*2 for k in l2]])
	print (res)
mult_poly(l1,l2)




class Polynomial():
	solve = []
	
	def __init__(self,l1,l2):
		self.l2 = l2
		self.l1 = l1

	def __str__(self):
		for i in self.solve:
			return i
	
	def __add__(self,l1,l2):
		'''	Adds two polynomials which are in a list form. '''
		self.l1 = list(reversed(self.l1))
		self.l2 = list(reversed(self.l2))

		self.solve = []

		if len(self.l1) > len(self.l2):
			self.l2 , self.l1 = self.l1 , self.l2  # swap if it is bigger.

		for i in self.l2:
			self.solve.append(i)

		for k in range(len(self.l1)):
			self.solve[k] = self.solve[k] + self.l1[k]#adds two numbers on the same list
		return self.solve

	def __mul__(self,l1,l2):
		return l1 * l2 #needs to be tested.






a = Polynomial(l1,l2)
# print (a.__add__(l1 , l2))

