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
		column = 0
		for row in range(0,self.length):
			for column in range(0,self.length):

				if self.queen_in_danger(row,column):

					self.board[row][column] = True

					if row == self.length:
						return None

					else:
						self.queen_in_danger(row-1,column-1)

	def queen_in_danger(self,row,column):
		''' True if the queen is safe  to be placed'''

		board = self.board	

		for k in range(self.length):# Row 

			if  board[row][k]  == True:
				return False

		for s in range(self.length): # Column

			 if board[s][column]== True:
			 	return False

		for m in range(row,self.length-1,1): #diagonal 

			print (row+m,column+m)
			if board[row+m][column+m] == True:
				return False

		for d in range(row,0,-1): #diagonal backwards

			if board[row-d][column-d] == True:
				return False

		return True


	def __str__(self):
		''' print the Boad if print method is called'''

		return ('\n\n'.join(['\t'.join(['{}'.format(number) for number in row]) for row in self.board]))


if __name__ == '__main__':
	a = Eight_Queens(8)
	a.solve()
	print (a)



