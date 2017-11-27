'''
1) In Danger!

Row1 = Row2

Column1 = Column2

|Row1-Row2| = |Column1 - Column2|

2) Peudsocode

if rows are the same

if columns are the same 

if ubstraction of row and columns is 0 


else return True.

'''


class Eight_Queens:
	'''Place Eight chess-queens without killing earch other.'''

	def __init__(self,length):
		# Matrix  length X length 
		self.length  =  length
		self.board = [[(k,i) for i in range(self.length)] for k in range(self.length)]
		self.solutions = []

	def solve(self):
		''' keeps calling queen_in_danger() since all queens is safe.'''
		row = -1
		for i in range(self.length):
			if self.queen_in_danger(row):

				self.solutions.append(self.board[row][i])
				self.board[row][i] = True 
				if i == self.length:
					return self.print_sol()

				else:
					self.queen_in_danger(row + 1)
			row +=1

	def queen_in_danger(self,row):
		''' True if the queen is safe '''
		board = self.board	

		for k in range(self.length):# Row

			if board[row][k] == True:
				return False

		for row in range(self.length):#Diagonal

			if board[row][row] == True:
				return False

		for k in range(self.length):#column

			if board[k][row] == True:
				return False

		return True

	def print_sol(self):
		for i in self.solutions:
			print ('this is a place.{}'.format(i))
	def __str__(self):

		return ('\n'.join([' '.join(['{}'.format(number) for number in row]) for row in self.board]))


if __name__ == '__main__':
	a = Eight_Queens(8)
	a.solve()
	a.print_sol()
	print (a)