'''
1. Consider a n x m matrix, with elements decimal digits
(natural numbers between 1 and 9), representing
colours.

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
from collections import Counter
import random as rnd

class Matrix:
    ''' Creates a matrix (n x m) of numbers and prints if there is any set,
        and which colour is the set of numbers '''

    def __init__(self,n,m):

        self.n = n
        self.m = m
        self.c = Counter({})
        self.colour = ['red','yellow','green','pink','grey','orange','blue','black','white']

    def create_matrix(self,n,m):
        ''' creates the matrix according to the inputs. '''

        self.mat = [[rnd.randint(1,9) for i in range(n)] for i in range(m)] # creates a matrix ! n x m
        print('\n'.join([' '.join(['{}'.format(number) for number in row]) for row in self.mat]))
        return self.mat

    def check_set(self):
        '''set will be checked '''
        matrx = self.mat

        for row in range(len(matrx)-1):

            for i in range(len(matrx[row])-1):

                if matrx[row][i] == matrx[row][i+1]: # checking the next intance
                    self.c.update({self.colour[matrx[row][i]-1]})#-1,to cover 0 instance in colour list. 

                if matrx[row][i] == matrx[row+1][i]: # checking the row's  next intance
                    self.c.update({self.colour[matrx[row][i]-1]})

                if row == len(matrx) - 2: # checking the corners of the matrix

                    if matrx[row+1][i] == matrx[row+1][i+1]:
                        self.c.update({self.colour[matrx[row+1][i]-1]})

                if i == len(matrx[row]) - 2:

                    if matrx[row][i+1] == matrx[row+1][i+1]:
                        self.c.update({self.colour[matrx[row+1][i+1]-1]})


        return self.c


    def print_colour(self):

        for values,keys in self.c.most_common(1):
            print ('the colour is {}. while the biggest set was {}.'.format(values,keys+1))


if __name__ == '__main__':

    try:
        n = int(input('type the column\t'))
        m = int(input('type the rows\t'))
        a = Matrix(n,m)
        a.create_matrix(n,m)
        a.check_set()
        a.print_colour()

    except (TypeError,ValueError):
        print ('type a number.')
