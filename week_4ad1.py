'''
1. Consider a n x m matrix, with elements decimal digits
(natural numbers between 1 and 9), representing
colours. Done!

A connected set associated to an element is the set of elements that
may be reached from this
element, by successive moves on a same row or column preserving the same color.
It is to determine the size and the colour of the biggest connected set.
In case of multiple solutions, display them all.
Input: n = 5 m = 6 and the values within the matrix are randomised, between 1 and 9)

                                        1 3 5 6 6 6
                                        8 8 5 2 2 2
                                        2 8 8 3 4 1
                                        7 1 8 5 9 9
                                        9 8 3 4 2 2

Output: The size of the biggest set is 5 and the colour is whichever colour you
represented by 8.

'''
import random as rnd

class Matrix:
    ''' Create a matrix according to inputs '''


    def __init__(self,n,m):
        self.n = n
        self.m = m

    def make_matrix(self,n,m):

        self.mat = [[rnd.randint(1,9) for i in range(n)] for i in range(m)] # creates a matrix ! n x m
        print('\n'.join([''.join(['{:2}'.format(number) for number in row]) for row in self.mat]))
        return self.mat

    def check_set(self):
        lst = self.mat

        for row in range(len(lst)):
            for i in range(len(lst[row])-1):
                if lst[row].count(lst[row][i]) >= 2 and lst[row][i] == lst[row][i+1]:

                    print('this: {}'.format(lst[row][i]))

                # elif self.mat[row].count(self.mat[row][i]) >= 2:
                    # print ()


    def print_colour(self,m):
        colour = ['red','yellow','green','pink','grey','orange','blue','violet','aqua','black','white']
        if self.m <= 0:
            return None
        else:
            m = m - 1
            return colour[m]


if __name__ == '__main__':

    try:
        n = int(input('type the column\t'))
        m = int(input('type the rows\t'))
        a = Matrix(n,m)
        a.make_matrix(n,m)
        a.check_set()
        print (a.print_colour(2))

    except (TypeError,ValueError):
        print ('type a number.')
