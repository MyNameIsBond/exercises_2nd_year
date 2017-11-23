
'''
b) Given the following pseudocode, first understand how it works, 
then implement the code for multiplying
the two polynomials in the programming language of your choice.
• Create a result array Res[], of size m + n + 1, 
where m is the degree of the first polynomial and n is
the degree of the second polynomial

• Initialise all the array elements as 0

• For each element of P1 (corresponding to index i) and each element of P2 
(corresponding to index j), perform the following operation

res[i+j] = res[i+j] + P1[i]*P2[j], where i is the index for P1 and j is the index for P2.

Hint: Use a nester FOR loop to traverse both arrays.

• Return res

'''
class Polynomial:
	'''can add and multiply Polynomails.'''
	
	def __init__(self,l1,l2):
		self.l2 = l2
		self.l1 = l1
		self.res = []

	def __str__(self):
		return self.res
	
	def __add__(self):
		'''	Adds two polynomials which are in a list form. '''
		self.l1 = list(reversed(self.l1))
		self.l2 = list(reversed(self.l2))
		self.res = []

		if len(self.l1) > len(self.l2):
			self.l2 , self.l1 = self.l1 , self.l2  # swap if it is bigger.

		for i in self.l2:
			self.res.append(i)

		for k in range(len(self.l1)):
			self.res[k] = self.res[k] + self.l1[k]
		return list(reversed(self.res))

	def __mul__(self):
		self.res = [0 for i in range(len(self.l1)+len(self.l2)-1)]
		for i in range(len(self.l1)):
			for j in range(len(self.l2)):
				self.res[i+j] = self.res[i+j] + self.l1[i]*self.l2[j]
		return list(reversed(self.res))



if __name__ == '__main__':
	l1 = [3,1,9]
	l2 = [2,1,2,1]
	a = Polynomial(l1,l2)
	print (a.__mul__())
	print (a.__add__())
