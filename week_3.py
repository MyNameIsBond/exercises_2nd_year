#--------->	this is week 3 on recursion. Enjoy!	<---------#
# -------------------------  ex1  ------------------------------- # 

# ---------------------------- if you want to run it uncomment the inputs lines 25 - 26 - 27 -------------------------------#





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




'''
Write a recursive version of linear search on an array of integers. What is the time complexity of the
algorithm? Use the BigO notation to express it.
Example input: L = [3,5,7,1,2,9] Target = 5
Example output: Found (or Yes or True etc)
Example input: L = [3,5,7,1,2,9] Target = 10
Example output: Not found (or No or False etc)
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
	if leng <= 5: # 5 is how many numbers the user is asked to type in. 
		try:
			given_number = int(input('Give me 5 numbers for my list '))
			print('countdown,{}'.format(leng))
			l.append(given_number)
			return linear_recursive_2nd(l,target,leng+1) # -1from leng so we can get out of the recursion
		except ValueError:
			print('Do not make me repeat my self')
	else:
		if target in l:
			print ('\t:{} Has been found'.format(target))
		else:
			print ('\t:{} Has not been found'.format(target))			



# try:
# 	target = int(input('For what number are you looking for?\t'))
# 	l = []
# 	linear_recursive_2nd(l,target,0)
# except (NameError,ValueError): # make sure the input is a number (int) 
# 	print ('a number please.')

		

#------------------------ Advanced ----------------------------#
'''
Consider having n cubes, each being characterized by their edge length and their colour. Use the cubes
to build a tower of maximum height, under the following conditions:
a) Any two neighbouring cubes must be of different colours.
b) The edge length of a cube is lower than the edge length of the cube placed below it.
Example input: n = 3
 cube1: colour red, edge length 5
 cube2: colour red, edge length 6
 cube3: colour blue, edge length 5
Example output: 16 (maximum tower height – corresponding to cube2, cube3 and cube1 in this order)

'''

def tower_of_cubes():
	''' Creates a tower of cubes '''

	cubes 	= {} # dict to store [name : [ colour : cube's length] ] 
	colours = ['red','pink','white','green','silver','black','orange']
	sum_length 	= 0
	try:
		n = int(input('how big your tower should be?\t'))
	except ValueError:
		print ('should be a number')
		
	for i in range(n):
		colour = int(input('Pick one from 1 to 7\t{}'.format(colours)))
		cube_length = int(input('Type a the length of the {} cube\t:'.format(colours[colour - 1])))
		cubes.update({'cube'+ str((i+1)):{colours[colour - 1]:cube_length}})
	for name,colour in cubes.items():
		for name_of_colour,cube_length in colour.items():
			sum_length += cube_length
			print ('{}\t{}'.format(name_of_colour,cube_length))
	print (cubes,sum_length)

tower_of_cubes()