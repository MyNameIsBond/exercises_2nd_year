import sys







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


