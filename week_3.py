# -------------------------ex1 ---------------------------------- # 





def prints_backwards(number,string):
	''' Prints a string seperated by spaces.'''
	if number <= 0:
		return None
	else:
		if type(string) == str:
			string = string.split(' ')
			print (number)
			for i in range(len(string)):
				s = string[i]
				s = s[::-1]
				print (s)
		# string = reversed(string)
		print ('\t:{}'.format(string[number]))
		prints_backwards(number-1,string)



string = input ('Give a string to be mirrored\t')

prints_backwards(4,string)