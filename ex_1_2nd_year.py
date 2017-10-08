
import re




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
    number_list = [1, 4, 7, 9]
    for n in number_list:
        if eval("n") > 0:
            int(re.search(r'\d+', n).group())
        elif eval("n") == 0:
            print ("Oops!")
            
def binary(number_list):
    for n in number_list:
        n =  int(re.search(r'\d+', bin(n)[2:] ).group())
        print (n)

# binary(number_list)


def binary1():

    number_list = [1,4,7,9]
    for n in number_list:
        ns = bin(n).replace("0b","")
        if ns == ns[::-1]:
            print ("We've got a palindrome here:{1}. From this Number:{0}".format(n,ns))
            s = 0
            number_list.remove(n)
            for i in number_list:
                s = s+1
                print (i,s)

            # print("{} This is a palindrome".format(ns))
# binary1()

def binary_2():
    number_list = [1, 4, 7, 9]    
    """ takes a list an returns the Palindrome, and remove them afterwards """
    for n in number_list:
        # if bin(n).replace("0b","") ==  
        print(n)
# binary_2()


    

number_list = [45, 4, 7, 9]
def kaprekar_num(number_list):
   for i in number_list:
       ik = str(i**2)
       if len(str(ik)) > 1:
           firstpart, secondpart = ik[:len(ik)//2], ik[len(ik)//2:] 
           f = int(firstpart) + int(secondpart)
           if f == i:
               return i
kaprekar_num(number_list)

# from sympy import *

def equation(s):
    s.split()
    for i in s:
        print(i)

equation("2x + y + 3z = 14")

