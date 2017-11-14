class Node:
    ''' Create Linked list'''
    def __init__(self,data):
        self.data = data
        self.next = None

    def get_data(self):
        ''' get the data '''
        
        return self.data

    def get_next(self):
        ''' get the next element '''
        return self.next

    def set_next_node(self,newnext):
        ''' set the element'''

        self.next = newnext

    def set_data(self,newdata):

        self.data = newdata


class Linked_list:
    ''' can create a linked list. '''

    def __init__(self,head=None):
        self.head = head


    def append(self,data):

        new_node = Node(data)
        new_node.set_next_node(self.head)
        self.head = new_node

    def empty(self):

        return self.head == None
        

    def delete(self,data):
        ''' Deletes an instance in the linked list '''

        current_node  = self.head
        previous_node = None
        found = False
        while not found:
            if current_node.get_data() == data:
                found = True
            else:
                current = current_node.get_next()
        if current_node == None:
            self.head = current.get_next()
        else:
            previous_node.set_next_node(current.get_next())

    def len(self):
        ''' return the length of the list. (int) '''

        current_node = self.node
        counter = 0
        while current_node != None:
            counter += 1
        return result

            
    def __str__(self):
        ''' prints out the list. '''
        result =  ','
        node = self.head
        if node != None:
            result +=','+ str(node)
            
            while node:
                result +=','+ str(node)
                node = node.get_next()

        return result



if __name__ == '__main__':
    my_list = Linked_list()
    my_list.append(4)
    my_list.append(5)
    my_list.append(6)
    my_list.append(7)
    print (my_list)
