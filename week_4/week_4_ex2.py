
# ----------------------------------- week 4, ex 2. ----------------------------------- #

'''
2. Use binary search in implementing a guessing game.
One thinks of a number between 1 and 20000, the
Program attempts to guess the number.
Feedback is given whether the number is higher or lower.
The program then makes a new guess and so on until it guesses the right numberself.
'''

import random as ran
class Guessing_game:
    ''' Guessing a Number using binary search '''

    def __init__(self,num_list,number):
        self.num_list = num_list
        self.number = number

    def binary_search(self,num_list):
        last = len(self.num_list)-1
        first = 0
        found = False
        while first <= last and not found:
            mid = (first + last) // 2
            if self.num_list[mid] == value:
                return True
            else:
                if value < self.num_list[mid]:
                    last = mid - 1
                else:
                    first = mid + 1
        return found
    def binary_search_No2(self,num_list,number):
        ''' a random number will be search in a random list. '''

        first = 0
        last = len(self.num_list) - 1

        if number > num_list[last]:
            print ('{} is too big.'.format(number))
        elif number < num_list[first]:
            print ('{} too small'.format(number))
        elif number in num_list:
            print ('I am gonna find {}'.format(number))
            while first <= last:
                mid = (first + last) // 2

                if num_list[mid] == self.number:
                    print ('The number was found!')
                    return True

                elif self.num_list[mid] > self.number:
                    last = mid - 1

                else:
                    first = mid + 1

        print ('not found.')

    def check_number(self):
        return

    def __str__(self):
        return str('your input:{}\n list: {}'.format(self.number,self.num_list))

if __name__ == '__main__':
    for i in range(10):
        number   = ran.randint(1,20000)
        num_list = [a for a in range(1,100)] # a list with random numbers
        a        = Guessing_game(num_list,number)
        a.binary_search_No2(num_list,number)
