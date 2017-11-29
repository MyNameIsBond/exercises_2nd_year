'''
1) In Danger!

Row1 = Row2

Column1 = Column2

|Row1-Row2| = |Column1 - Column2|

2) Peudsocode

if rows are the same

if columns are the same 

if ubstraction of row and columns is same

else return True.
'''


class Eight_Queens:
	'''Place Eight chess-queens without killing earch other.'''

	def __init__(self,length):
		# Matrix  length X length 
		self.length  =  length
		self.board 	 = [[(k,i) for i in range(self.length)] for k in range(self.length)]
		self.solutions = []

	def solve(self):
		''' keeps calling queen_in_danger() since all queens is safe.'''
		for row in range(self.length):

			for column in range(self.length):

				if self.queen_in_danger(row,column):

					self.board[row][column] = True
					self.solutions.append((row,column))
					if len(self.solutions) == self.length:
				else:
					self.queen_in_danger(row-1,column)

	def queen_in_danger(self,row,column):
		''' True if is the right place. '''

		board = self.board	

		for k in range(self.length):# Column_check 

			if  board[row][k]  == True:
				return False

			if board[k][column]== True: # Row 
				return False

			if self.diagonal_queen(row,column): # Diagonal.
				return False

		return True

	def diagonal_queen(self,row1,column1):
		''' true if the Queen is not safe '''
		for c_row in range(self.length):

			for c_column in range(self.length):

				current = self.board[c_row][c_column]

				if type(current) == bool:
					cur_row = abs(row1 - c_row)
					cur_col = abs(column1 - c_column)

					if cur_col == cur_row:

						return True


	def solution(self):
		'''return the queen's position so it can be tested.'''
		return self.solutions

	def __str__(self):
		''' print the Boad if print method is called'''

		return ('\n\n'.join(['\t'.join(['{}'.format(number) for number in row]) for row in self.board]))



if __name__ == '__main__':
	try:
		a = Eight_Queens(8)
		a.solve()
		print (a)
	except TypeError:
		print ('The input should be a number.')