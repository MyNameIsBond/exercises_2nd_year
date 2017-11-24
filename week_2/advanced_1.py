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
import numpy as np


class Eight_Queens:
	'''Place Eight chess-queens without killing earch other.'''

	def __init__(self,length):
		# self.board = [[0 for i in range(length)] for i in range(length)]
		# length = (length,length)

		
		self.board = [[1,2 ,3 ,4 ,5 ,6 ,7 ,8 ],
					 [ 9,10,11,12,13,14,15,16],
				 	 [17,18,19,20,21,22,22,23],
				 	 [21,22,23,24,25,26,25,24],
				 	 [31,32,33,34,35,36,37,38],
				 	 [41,42,43,44,45,46,47,48],
				 	 [51,52,53,54,55,56,57,58],
				 	 [61,62,63,64,65,66,67,68]]

		# self.board = np.zeros(length,dtype=np.int)




	def safe_place(self):
		'''True is the queen is safe.'''
		board = self.board
		counter = range(len(board))
		for row in counter:			
			print(board[row][row])

		for row in counter:
			print ('{}'.format(board[row][]))


	def print_board(self):
		''''''
		pass

	def __str__(self):
		return str(self.board)


if __name__ == '__main__':
	a = Eight_Queens(8)
	a.safe_place()