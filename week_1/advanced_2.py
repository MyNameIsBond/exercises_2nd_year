
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
    cost		= (4,7,15)
    used_mat    = {}
    print('mater\tOwn\tQua\tKg\tGiven Kg:{}'.format(carried_kg))
    print ('----------------Calculation-----------------')
    price,counter = 0,0
	
    for m,q in material.items():
        carried_kg,nq = max(0,carried_kg - q),max(0,q-carried_kg)

        if q > nq:
            price = ((q-nq) * cost[counter]) + price
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
