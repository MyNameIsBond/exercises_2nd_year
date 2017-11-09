'''
1. Consider a n x m matrix, with elements decimal digits (natural numbers between 1 and 9), representing
colours. A connected set associated to an element is the set of elements that may be reached from this
element, by successive moves on a same row or column preserving the same color. It is to determine
the size and the colour of the biggest connected set. In case of multiple solutions, display them all.
Input: n = 5 m = 6 and the values within the matrix are randomised, between 1 and 9)

                                        1 3 5 6 6 6
                                        8 8 5 2 2 2
                                        2 8 8 3 4 1
                                        7 1 8 5 9 9
                                        9 8 3 4 2 2

Output: The size of the biggest set is 5 and the colour is whichever colour you represented by 8.
'''
import random as rnd
class MMatrix:
    ''' Create a matrix according to inputs '''


    def __init__(self,n,m):
        self.n = n
        self.m = m

    def make_matrix(self,n,m):
        colour = ['red','yellow','green','pink','grey','orange','blue','violet','aqua','black','white']
        mat = [[rnd.randint(1,9) for i in range(n)] for i in range(m)] # creates a matrix! n x m
        print('\n'.join([''.join(['{:2}'.format(number) for number in row]) for row in mat]))

if __name__ == '__main__':
    try:
        n = int(input('type the length(rows)\t'))
        m = int(input('type the width(column)\t'))
        a = MMatrix(n,m)
        a.make_matrix(n,m)
    except TypeError:
        print ('type a number.')
