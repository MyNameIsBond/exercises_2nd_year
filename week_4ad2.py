
'''2. Adapt the Quick Sort algorithm to find the mth smallest element out of a list of n integers, where m is
read from the standard input.
For example, when m = 5, your version of Quick Sort will output the 5th smallest element out of your
input list.'''

from random import randint as rint
class Smallest:
    ''' The smallest (number)th element will be printed out. using quick sort'''
    def __init__(self,number):
        self.number      = number
        self.random_list = [rint(1,20) for x in range(rint(1,20))] # create a random list.


    def quick_sort(self):
        '''the quick sort'''

        for i in self.random_list:
            print (i)


if __name__ == '__main__':
    a = Smallest(5)
    a.quick_sort()
