
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

from collections import OrderedDict

def tower_of_cubes():
	''' Creates a tower of cubes '''

	cubes 			= {} # dict to store [name : [ colour : cube's length] ]
	colours 		= ['red','pink','white','green','silver','black','orange']
	sum_length 		= 0
	colour_check	= None # a variable to check the colour looping thought the sorted list.
	counter 		= 0

	try:
		n = int(input('how big your tower should be?\t'))
	except ValueError:
		print ('should be a number')

	for i in range(n):
		colour 		= int(input('Pick one colour from 1 to 7\t{}'.format(colours)))
		cube_length = int(input('Type a the length of the {} cube\t:'.format(colours[colour - 1])))
		cubes.update({'cube'+ str((i+1)):{'length':cube_length,'colour':colours[colour - 1]}})
		sum_length += cube_length
		
	final_list = sorted(cubes, key=lambda x: cubes[x]['length'])

	for i in final_list:

		if colour_check == None:
			colour_check = cubes[i]['colour']

		elif colour_check != cubes[i]['colour']:
			colour_check = cubes[i]['colour']

		elif colour_check == cubes[i]['colour']:

			if final_list[counter+1] == True:
				final_list[counter] , final_list[counter+1] = final_list[counter+1], final_list[counter] # swapping.
			else:
				final_list[counter-1] , final_list[counter-2] = final_list[counter-2], final_list[counter-1] # swapping.

		counter +=1
		
	print ( str(sum_length) +'  ' +'  '.join(reversed(final_list)))



if __name__ == '__main__':
	tower_of_cubes()
