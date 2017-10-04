import sys




"""
1. Write a function that deletes a substring from a given character string, specifying the beginning
position and the length of the substring.


"""


def del_substring():
    person = input('Enter your string: ')
    hey = list(person)
    print ("This is how many charachters you gave me :" + str(len(hey)))
    for i in hey:
        print(i)
    deleted = input('Enter the substring you want to delete: ')
    hey.remove(deleted)
    for i in hey: 
        print(i)
#del_substring()



"""
2. Read from the keyboard a list of positive integers, for example: 1, 4, 7, 9
a. Write a function that prints the binary representation of the numbers in the list, for the example
above it is: 1: 0001 4: 0100 7: 0111 9: 1001
b. Print the numbers from the previous list that are palindromes. For example, 9: 1001 is a
palindrome.
c. Remove all the numbers in the list whose binary representation is a palindrome and print the list
after their removal.
"""
def positive():
    number_list = [1,2,3,4,5,6,7,8,9,-2,-13,0]
    for n in number_list:
        if eval("n") > 0:
            print(str(n) + "plus")
        elif eval("n") == 0:
            print ("Oops!")
positive()