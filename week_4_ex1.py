#--------------------------------------------week 4--------------------------------------------#
'''
 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   ex 1   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
Manually arrange the sequence [2 7 9 4 1 5 3 6 0 8] in ascending order using insertion sort, bubble sort
and selection sort, showing at each step the new configuration of the sequence. How many
comparisons and how many element moves were used by each method? Which is the best performing
method for sorting this array of integers? Which would be the worst arrangement of this sequence?



1) Insertion Sort:
Bellow you will find the code for insertion sort is in the class 'All_sorts' (inserion).
basically this is, a slow sorting algorithm when it comes to sort a large list. 
The steps are preatty simple. 
In a unsorted list fist checks the 2st element and if it's smaller then the previous(1st element) swapp it.
otherwise move it to the next element of the list...
according to my comparisons_counter, this algorithm is going to compare 18 times.
the worst performance is if the list is large. The best perfomance would be with a small list.
this could be explained: Best case:O(n) which means O(1) one swapp. worst case: O(n^2) or ( O(n**2) ) 
If you run the inserion function the swappings will be printed as well as the steps. 

2)selection_sort:
worst and best case scenario is O(n^2) or O(n**2)
the explaination is simple, goes through the list if by comparing finds the smallest which takes it and swapp it in the
1st place of the list (list[0]) and does the same,but this time by starting from list[1] and goes on. until the list is sorted
to run selection sort. selection_sort() in class All_sorts should be run.


3) bubble sort:
this could be explained: Best case:O(n) which means O(1) one swapp. worst case: O(n^2) or ( O(n**2) ) 
this algorith is the slowest in this list. because compares only two numbers at a time.
'''
class All_sorts:
    ''' every function is another sort type (algorithm). '''

    def __init__ (self,num_list):
        self.num_list = num_list
        
    def insertion(self,num_list):
        '''insertion sort:in a list of numbers checks and swaps if the comparing element is less than. '''

        swapping_counter = 0  # this var is used to count the swappings.
        counter          = 0  #this var is used to count how many times the algo is passing through the loops.
        bc               = 1  # bc = big counter. which means is used out of the nested while loop.
        list_len         = len (self.num_list)

        while bc < list_len:
            counter += 1
            sc = bc   # sc = small counter. which means is used as a counter in the nested while loop.  

            while sc > 0 and self.num_list[sc-1] > self.num_list[sc]:
                counter += 1

                if sc > 0 and self.num_list[sc-1] > self.num_list[sc]: # so we can print wither is swapped or not.
                    swapping_counter +=1 # this is the counter on weither the swapping occured.
                    print ('{}) {} and {} were swapped.  {}'.format(swapping_counter,self.num_list[sc-1],self.num_list[sc],num_list))
                self.num_list[sc-1], self.num_list[sc] = self.num_list[sc], self.num_list[sc-1]
                sc -= 1

            bc += 1
        print ('|{}| This is how many times this alth run'.format(counter))
        return self.num_list    
    
    
    def bubble_sort(self,num_list):
        ''' a bubble sort algorithm '''
        swapping_counter = 0    # this var is used to count the swappings.
        counter          = 0    #this var is used to count how many times the algo is passing through the loops.
        m                = len(num_list)
        while m > 0:
            counter += 1 

            for i in range(1,m): # starts from one in order to avoid errors. 
                counter += 1 
                if self.num_list[i-1] > self.num_list[i]:
                    swapping_counter += 1
                    self.num_list[i-1] , self.num_list[i] = self.num_list[i] , self.num_list[i-1]
                    print ('{}) {} and {} were swapped. list:{}'.format(swapping_counter,self.num_list[i-1] , self.num_list[i],num_list))
            m -= 1
        print ('|{}| This is how many times this alth run'.format(counter))
        return self.num_list

    def selection_sort(self,num_list):
        ''' selection sort algorithm ''' 
        swapping_counter = 0    # this var is used to count the swappings.
        counter          = 0    #this var is used to count how many times the algo is passing through the loops.
        n = len(self.num_list)
        for s in range(n):
            counter += 1

            for k in range(s,n):
                counter += 1

                if self.num_list[k] < self.num_list[s]:
                    swapping_counter += 1
                    self.num_list[k],self.num_list[s] = self.num_list[s] , self.num_list[k] 
                    print ('{}) {} and {} were swapped. while the list is {}'.format(swapping_counter,self.num_list[k],self.num_list[s],num_list))

        print ('|{}| This is how many times this alth run'.format(counter))
        return self.num_list

    def __str__(self):
        ''' prints the list '''
        return str(self.num_list)


# To Check every sorting,uncomment instances one at a time. (lines: 91,92,93,94)
if __name__ == '__main__':
    try: # to make sure is going to be a list.
        l = [2,7,9,4,1,5,3,6,8,0]
        a = All_sorts(l)
        a.insertion(l)
        # a.bubble_sort(l)
        # a.selection_sort(l)
        # print (a)
    except TypeError:
        print('a list should be given should be given.')



# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< end of the 1st ex.  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>