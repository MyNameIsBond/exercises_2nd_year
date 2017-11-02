#--------------------------------------------week 4--------------------------------------------#
'''
Manually arrange the sequence [2 7 9 4 1 5 3 6 0 8] in ascending order using insertion sort, bubble sort
and selection sort, showing at each step the new configuration of the sequence. How many
comparisons and how many element moves were used by each method? Which is the best performing
method for sorting this array of integers? Which would be the worst arrangement of this sequence?
insertion       | Done! 
bubble sort     | Done!
selection sort  | Not yet.

'''
'''
1) 
Bellow you will find the code for insertion sort.
basically this is, a slow sorting alg. 
The steps are preatty simple. 
In a unsorted list fist it checks the 1st element and if the next element in the list is smaller swaps with the previous.
according to my comparisons_counter, this algorithm is going to compare 18 times.
the worst performance is if the list is very big. The best perfomance would be with a small list.  

'''
class All_sorts:
    ''' every function is another sort. '''

    compare_number  = None
    loop_counter    = 0

    def __init__ (self,num_list):
        self.num_list = num_list
        
    def insertion(self,num_list):
        '''insertion sort for a list of numbers'''
        list_len = len (self.num_list)
        bc = 1  # bc = big counter. which means is used out of the nested while loop.
        comparisons_counter = 0 # in order to count the comparisons.

        while bc < list_len:
            comparisons_counter += 1
            sc = bc   # sc = small counter. which means is used as a counter in the nested while loop.  

            while sc > 0 and self.num_list[sc-1] > self.num_list[sc]:
                self.num_list[sc-1], self.num_list[sc] = self.num_list[sc], self.num_list[sc-1]
                sc -= 1
                comparisons_counter += 1

            bc += 1
            print (comparisons_counter)
        print (self.num_list)
        return self.num_list
    
    def bubble_sort(self,num_list):
        ''' a bubble sort algorithm '''
        m = len(num_list)
        while m > 0:

            for i in range(1,m):
                if self.num_list[i-1] > self.num_list[i]:
                    self.num_list[i-1] , self.num_list[i] = self.num_list[i] , self.num_list[i-1]
            m -= 1
        print ('this is the list sorted\t:{}'.format(self.num_list))

    def selection_sort(self,num_list):
        '''
        for i = 0 to numItems - 1
            for  j = i+1 to numItems               
                if A[i] > A[j]
                    // Swap the entries
                    Temp = A[i]
                    A[i] = A[j]
                    A[j] = Temp          
                End If    
            Next j
        Next i
        ''' 
        n = len(num_list)
        i = 0

        for s in range(n):
            for k in range(s,n):
                if num_list[k] < num_list[s]:
                    num_list[k],num_list[s] = num_list[s] , num_list[k] 
                    
        print (num_list)
        return num_list


    def __str__(self):
        return 'use one of my functions.\n insertion(list) , bubble_sort(list) '


l = [4,5,6,2,8,1,34,5,6,2,8,1,34,5,6,2,8,1,34,5,6,2,8,1] 

a = All_sorts(l)
# a.insertion(l)
# a.bubble_sort(l)
a.selection_sort(l)
