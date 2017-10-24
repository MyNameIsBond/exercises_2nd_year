# -------------------------ex1 ---------------------------------- # 
x = input ('Give a string to be mirrored\t')

def prints_backwards(x):
	''' Prints a string seperated by spaces.'''
	x = x.split(' ')

	for i in x:
		print (i[::-1]) # printing backwards the string.
prints_backwards(x)
