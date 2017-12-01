
'''
2. Adapt the Quick Sort algorithm to find the mth smallest element out of a list of n integers, where m is
read from the standard input.
For example, when m = 5, your version of Quick Sort will output the 5th smallest element out of your
input list.
'''

from random import randint as rint
class Smallest:
    ''' The smallest (number)th element will be printed out. using quicksort'''

    def __init__(self,number):

        self.number = number
        self.r_list = [rint(1,20) for x in range(rint(10,20))] # create a random list.

        lower = 0
        high  = len(self.r_list) - 1
        self.quicksort(lower,high)


    def quicksort(self,lower,high):
        '''the Quicksort.'''

        if lower < high:
            p = self.partition (lower,high)
            self.quicksort(lower,p - 1)
            self.quicksort(p+1,high)

    def partition(self,lower,high):
        ''' break the list. '''

        pivot = self.r_list[high]
        wall = lower - 1
        for j in range(lower,high):

            if self.r_list[j] < pivot:
                wall = wall + 1
                self.r_list[wall],self.r_list[j] = self.r_list[j],self.r_list[wall]

        if self.r_list[high] < self.r_list[wall + 1]:
            self.r_list[wall + 1],self.r_list[high] = self.r_list[high],self.r_list[wall + 1]

        return wall + 1

    def check_number(self):
        '''print out the index of the given number. '''

        if (len(self.r_list)-1) > self.number:
            small   = self.r_list[self.number-1]
            el_list = self.number
            print ('{}, is the {}th smallest element | Given number {}'.format(small,el_list,self.number))

        else:
            print ('The list is too small for the given number.')

    def __str__(self):
        '''prints out the list. '''
        return str(self.r_list)


if __name__ == '__main__':
    try:
        a = Smallest(5)
        a.check_number()
        print (a)

    except (TypeError,ValueError):
        print ('the Input should be a number.')


