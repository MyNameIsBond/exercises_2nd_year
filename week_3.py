#--------->	this is week 3 on recursion. Enjoy!	<---------#
# -------------------------  ex1  ------------------------------- # 

#---------------------------- if you want to run it uncomment the inputs lines 25 - 26 - 27 -------------------------------#





def prints_backwards(number,string):
	''' Prints a string seperated by spaces.'''
	
	if number <= -1: # this is the way out. 
		return None

	else:
		if type(string) == str:
			string = string.split(' ')
			if number < len(string):
				number = len(string) - 1 # make sure the function will run.
				print (number)
		print ('\t:{}'.format(string[number][::-1]))
		return prints_backwards(number-1,string)

string = input ('Give a string to be mirrored\t')
prints_backwards(1,string)




'''# Write a recursive version of linear search on an array of integers. What is the time complexity of the
# algorithm? Use the BigO notation to express it.
# Example input: L = [3,5,7,1,2,9] Target = 5
# Example output: Found (or Yes or True etc)
# Example input: L = [3,5,7,1,2,9] Target = 10
# Example output: Not found (or No or False etc)
'''
# -------------------------  ex2  ------------------------------- # 
l =  [3,5,7,1,2,9]
def linear_recursive(l):
	target = int(input('give me a target\t'))
	if target in l:
		print ('{},Found!'.format(target))
	else:
		print ('{},Not Found!'.format(target))



# linear_recursive(l)

def linear_recursive_2nd(l,target,leng):
	''' you create a list and find a given number in the list '''
	if leng <= 5:
		try:
			given_number = int(input('Give me 10 numbers for my list '))
			print('countdown,{}'.format(leng))
			l.append(given_number)
			return linear_recursive_2nd(l,target,leng+1)
		except ValueError:
			print('Do not make me repeat my self')
	else:
		if target in l:
			print ('\t:{} Has been found'.format(target))
		else:
			print ('\t:{} Has not been found'.format(target))			

try:
	target = int(input('For what number are you looking for?\t'))
	l = []
	linear_recursive_2nd(l,target,0)
except (NameError,ValueError):
	print ('a number please.')

		
