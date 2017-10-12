def combine_str(string_no1, string_no2):
    """ Combines two strings and returns one output"""
    str_list = []
    for i in range(len(string_no1+string_no2)):
        if i <= (len(string_no1)-1):
            str_list.append(string_no1[i])
        if i <= (len(string_no2)-1):
            str_list.append(string_no2[i])
    return print("".join(str_list)) # makes the list(str_list) a string 

#combine_str("1dfghj34","5xjlkjlkj8")



"""
Check if a 3 digit number is an Armstrong number. 
An Armstrong number of three digits is an integer
such that the sum of the cubes of its digits
is equal to the number itself. 
For example, 371 is an
Armstrong number since 3**3 + 7**3 + 1**3 = 371."""

def armstrong_num(number):
    """ True if a given number is armstrong """
    ip = 0
    for i in map(int,str(number)):
        ip = ip + i**len(str(number))
        if number == ip:
            print("{},Is an armstrong".format(number))
armstrong_num(1634)
def test_armstrong():
    for number in range(1000):
        return armstrong_num(number)