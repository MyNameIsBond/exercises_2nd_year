
l1 = [3,1,9]
l2 = [2,1,2,1]

def polynomial(l1,l2):
	solve = []
	counter = -1
	for i,r in zip(l1,l2):
		solve.append(i + r)
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
