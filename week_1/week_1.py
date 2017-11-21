def combine_str(string_no1, string_no2):
    """ Combines two strings and returns one output"""
    str_list = []
    
    for i in range(len(string_no1 + string_no2)):

        if i <= (len(string_no1)-1):
            str_list.append(string_no1[i])

        if i <= (len(string_no2)-1):
            str_list.append(string_no2[i])

    return ("".join(str_list)) # makes the list(str_list) a string 



"""The factorial for a non-negative integer n, n!, is defined 
as: 0! = 1 n! = n * (n-1)! (n > 0). The input to
your program consists of several lines, 
each containing two non-negative integers, n and m, both less
than 2^31. For each input line, 
output a line stating whether or not m divides n!.

Example input: 
Example output:
9 divides 6!
27 does not divide 6!
10000 divides 20!
100000 doe not divide 20!
"""



def armstrong_num(number):
    """ True if a given number is armstrong """

    if number >= 2 and type(number)==int: # Try to make Try : except :
        ip,counter = 0,0

        for i in map(int,str(number)):
            counter = counter + 1            
            ip = ip + i**len(str(number))

            if number == ip:
                print("{}, Is an armstrong".format(number))
                return ("{}, Is an armstrong".format(number))

            elif len(str(number)) == counter:
                print("{}, It is not armstrong".format(number))
                return ("{}, It is not armstrong".format(number))

def factorial(m,n):
    n,m = int(n),int(m) # turned to int to compare them and divide
    if ((n or m) <= (2**31)):
        if (n % m == 0):
            print('{0:1d} Devides {1:2d}'.format(m, n))
    else:
        return print ("Nothing!")
factorial(2,4)

"""
A lorry can carry at most {n} kilograms. The name of the materials, 
the amount of material in kilograms
and the material price per kilo are known.
Compute a load composition in such a way that the value
(price) of the load is maximum. 


input:
N = 10     
Copper        7  kg      65     
Plastic       15 kg      50     
Gold          4  kg      100 
 
Output:Load composition value = 790      4 kg of gold and 6 kg of copper 
"""

def larry(carried_kg):
    ''' Takes KG and Print out according to storage how 
    much is being used and will be carried out from Larry  '''
    material	= {'Gold':6,'Copper':3,'Plastic':15}
    cost_l		= (10,5,2)
    used_mat    = {}
    print('mater\tOwn\tQua\tKg\tGiven Kg:{}'.format(carried_kg))
    print ('----------------Calculation-----------------')
    price,counter = 0,0
	
    for m,q in material.items():
        carried_kg,nq = max(0,carried_kg - q),max(0,q-carried_kg)

        if q > nq:
            price = ((q-nq) * cost_l[counter]) + price
        counter = counter + 1
        print('{}\t{}\t:{}\t{}'.format(m,q,nq,carried_kg))
        material[m] = (q - nq)
        used_mat.update({m : q-nq})

        if carried_kg == 0:
            break
    print ('--------------------------------------------\n')
    print ('----------------Have Been Used--------------')
    for k,t in used_mat.items(): 
        print ('{}\t\t:{}'.format(k,t))

    print('Kg Left:{}\tPrice:{}\n\n'.format(carried_kg,price))

    return (carried_kg,price)

