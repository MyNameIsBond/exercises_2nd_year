# -------------------------ex1 ---------------------------------- # 





def prints_backwards(number,string):
	''' Prints a string seperated by spaces.'''
	
	if number <= 0: # this is the way out. 
		return None

	else:
		if type(string) == str:
			string = string.split(' ')
			if number >= len(string):
				number = len(string) # make sure the function will run. 

		print ('\t:{}'.format(string[number][::-1]))
		return prints_backwards(number-1,string)

string = input ('Give a string to be mirrored\t')
number = int (input('How many times you want the recursion to run? :)\t'))
prints_backwards(number,string)