
class All_sorts:

    compare_number  = None
    loop_counter    = 0

    def __init__ (self,number_list):
        self.number_list = number_list
        
    def insertion(self,number_list):

        for i in range(len(self.number_list)):
            print (self.number_list[i])
            if self.compare_number == None:
                self.compare_number = i
                print ('oops!')



    # def bouble_sort(self,number_list):
l = [1,2,4,5,6,7,8] 

a = All_sorts(l)
a.insertion(l)

