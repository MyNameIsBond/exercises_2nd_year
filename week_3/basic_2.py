'''
Write a recursive version of linear search on an array of integers. What is the time complexity of the
algorithm? Use the BigO notation to express it.
Example input: L = [3,5,7,1,2,9] Target = 5
Example output: Found (or Yes or True etc)
Example input: L = [3,5,7,1,2,9] Target = 10
Example output: Not found (or No or False etc)
'''

def linear_recursive(l,counter,number):
	if number == l[counter]:
		return True
	elif counter == -1:
		return False	
	else:
		linear_recursive(l,counter-1,number)

if __name__ == '__main__':
    try:
        l =  [3,5,7,1,2,9]
        counter = len(l) - 1
        number = int(input('Give me the number you want to find.\t'))
        linear_recursive(l,counter,number)
    except TypeError:
        print('Give me a number please.')