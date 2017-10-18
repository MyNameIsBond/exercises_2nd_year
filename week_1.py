def combine_str(string_no1, string_no2):
    """ Combines two strings and returns one output"""
    str_list = []
    for i in range(len(string_no1 + string_no2)):
        if i <= (len(string_no1)-1):
            str_list.append(string_no1[i])
        if i <= (len(string_no2)-1):
            str_list.append(string_no2[i])
    return print("".join(str_list)) # makes the list(str_list) a string 

#combine_str("1dfghj34","5xjlkjlkj8")

def armstrong_num(number):
    """ True if a given number is armstrong """
    if number >= 2 and type(number)==int: # Try to make Try : except :
        ip,counter = 0,0
        for i in map(int,str(number)):
            counter = counter + 1            
            ip = ip + i**len(str(number))
            if number == ip:
                return print("{}, Is an armstrong".format(number))
            elif len(str(number)) == counter:
                print("{}, It is not armstrong".format(number))

armstrong_num(0)
def test_armstrong():
    for number in range(1000):
        return armstrong_num(number)

# test_armstrong()
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
def factorial(fact_number):
    m = input ("Give me one number M \n")
    n = input ("Give me one number N \n")
    n,m = int(n),int(m) # tured to int to compare them and divide
    if ((n or m) <= (2**31)):
        if (n % m == 0):
            print('{0:1d} Devides {1:2d}'.format(m, n))
    else:
        return print ("Nothing!")
factorial(2)
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

def ks_larry():
  material = {'gold':6,'Copper':3,'Plastic':15}
  carried_kg = int(input('How many kg you want to be carried out.'))
  print('mater\t Qua\tkg')
  print ('--------------------')
  for m,q in material.items():
  	carried_kg = max(0,abs(carried_kg - q))
  	q = q - carried_kg
  	if (q or carried_kg) >= 0:
  		print ('Bing!')
  	print('{}\t:{}\t{}'.format(m,q,max(0,carried_kg)))
  print ('--------------------')
  
  
  
  print('value:\t\t{}'.format(carried_kg))
ks_larry()
    
