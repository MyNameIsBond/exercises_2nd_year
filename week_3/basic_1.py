def prints_backwards(number,string):
	''' Prints a string backwards seperated by spaces.'''

	if number <= -1: # this is the way out.
		return None

	else:
		if type(string) == str:
			string = string.split(' ')
			if number < len(string):
				number = len(string) - 1 # make sure the function will run.
				print (number)
		print ('\t:{}'.format(string[number][::-1])) # print the list according to the 'number'
		return prints_backwards(number-1,string)

# string = input ('Give a string to be mirrored\t')
# prints_backwards(1,string)

if __name__ == '__main__':
    
    prints_backwards(1,string)






    
    