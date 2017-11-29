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


if __name__ == '__main__':
    try:
        target = int(input('For what number are you looking for?\t'))
        l = []
        linear_recursive_2nd(l,target,0)
    except (NameError,ValueError): # make sure the input is a number (int)
        print ('a number please.')
