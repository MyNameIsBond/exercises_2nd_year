#--------------------------------------------week 4--------------------------------------------#
'''
Manually arrange the sequence [2 7 9 4 1 5 3 6 0 8] in ascending order using insertion sort, bubble sort
and selection sort, showing at each step the new configuration of the sequence. How many
comparisons and how many element moves were used by each method? Which is the best performing
method for sorting this array of integers? Which would be the worst arrangement of this sequence?



1) 
Bellow you will find the code for insertion sort.
basically this is, a slow sorting algorithm when it comes to sort a large list. 
The steps are preatty simple. 
In a unsorted list fist it checks the 1st element and if the next element in the list is smaller swaps with the previous.
according to my comparisons_counter, this algorithm is going to compare 18 times.
the worst performance is if the list is large. The best perfomance would be with a small list.
this could be explained: Best case:O(n) worst case: O(n^2) or ( O(n**2) )   
so the swapping would be like this
step 1:[2 7 9 4 1 5 3 6 0 8]
step 2:[2 7 9 4 1 5 3 6 0 8]
step 3:[2 7 9 4 1 5 3 6 0 8]
step 4:[2 7 9 4 1 5 3 6 0 8]
step 5:[2 7 9 4 1 5 3 6 0 8]
step 6:[2 7 9 4 1 5 3 6 0 8]
step 7:[2 7 9 4 1 5 3 6 0 8]
step 8:[2 7 9 4 1 5 3 6 0 8]
2)
Bellow you will find the code for the Bubble Sort. 
This algorithm could be described as 
'''
class All_sorts:
    ''' every function is another sort type (algorithm). '''

    def __init__ (self,num_list):
        self.num_list = num_list
        
    def insertion(self,num_list):
        '''insertion sort for a list of numbers'''
        list_len = len (self.num_list)
        bc = 1  # bc = big counter. which means is used out of the nested while loop.
        while bc < list_len:
            sc = bc   # sc = small counter. which means is used as a counter in the nested while loop.  

            while sc > 0 and self.num_list[sc-1] > self.num_list[sc]:
                self.num_list[sc-1], self.num_list[sc] = self.num_list[sc], self.num_list[sc-1]
                sc -= 1

            bc += 1
        return self.num_list
    
    def bubble_sort(self,num_list):
        ''' a bubble sort algorithm '''
        m = len(num_list)
        while m > 0:

            for i in range(1,m): # starts from one in order to avoid errors. 
                if self.num_list[i-1] > self.num_list[i]:
                    self.num_list[i-1] , self.num_list[i] = self.num_list[i] , self.num_list[i-1]
            m -= 1
            
        return self.num_list

    def selection_sort(self,num_list):
        ''' selection sort algorithm ''' 
        n = len(self.num_list)
        for s in range(n):

            for k in range(s,n):

                if self.num_list[k] < self.num_list[s]:
                    self.num_list[k],self.num_list[s] = self.num_list[s] , self.num_list[k] 
                    
        return self.num_list

    def __str__(self):
        ''' prints the list '''
        return str(self.num_list)

l = [2 7 9 4 1 5 3 6 0 8]

a = All_sorts(l)
# a.insertion(l)
# a.bubble_sort(l)
a.selection_sort(l)
print (a)