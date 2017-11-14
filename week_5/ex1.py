class Node(object):
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

    def set_next_node(self,data):
        ''' set the element'''

        self.data = newdata


class Linked_list:
    '''can create a linked list. '''

    def __init__(self,head=None):
        self.head = head


    def append(self,data):
        new_node = Node(data)
        new_node.set_next_node(self.head)
        self.head = new_node
        

    def delete(self,data):
        '''Deletes an instance in the linked list'''

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
        current_node = self.node
        counter = 0
        while current_node != None:
            counter += 1
        return result

            
    def __str__(self):
        result =  []
        node = self.head
        while node != None:
            node = node.get_next()
            result.append(node)
        return result



if __name__ == '__main__':
    a = Linked_list.append(2)
    # a = Linked_list.set_data(4)
    # a = Linked_list.set_data(5)
    # a = Linked_list.set_data(6)
    print (a)




 