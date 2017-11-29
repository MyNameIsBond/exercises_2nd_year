"""The factorial for a non-negative integer n, n!, is defined 
as: 0! = 1 n! = n * (n-1)! (n > 0). The input to
your program consists of several lines, 
each containing two non-negative integers, n and m, both less
than 2^31. For each input line, 
output a line stating whether or not m divides n!.

Example input: 
6 9
6 27
20 10000
20 100000

Example output:
9 divides 6!
27 does not divide 6!
10000 divides 20!
100000 doe not divide 20!
"""

import math

def factorial(n,m):
	''' True if the factorial is devided with the m '''
	n_1 = n # store to print.
	fact = 1
	while n >= 1:
		fact = fact * n  
		n = n - 1
	
	if (fact % m) == 0:
		print ('{}! Devided {}'.format(n_1,m))
		return True
	else:
		print ('{}! Not Devided {}'.format(n_1,m))
		return False






# ----------------- Bonus solution -----------------

def bonus_factorial(n,m):
	'''another way of solving it. |build in method'''
	if (math.factorial(n) % m) == 0:
		print ('{}! Devided {}'.format(n,m))
		return True

	else:
		print ('{}! Not Devided {}'.format(n,m))
		return False


