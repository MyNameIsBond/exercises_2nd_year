def armstrong_num(number):
    """ True if a given number is armstrong """

    if number >= 2 and type(number)==int: # Try to make Try : except :
        ip,counter = 0,0

        for i in map(int,str(number)):
            counter = counter + 1            
            ip = ip + i**len(str(number))

            if number == ip:
                print("{}, Is an armstrong".format(number))
                return True

            elif len(str(number)) == counter:
                print("{}, It is not armstrong".format(number))
                return False