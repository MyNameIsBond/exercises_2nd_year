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

class Linked_list:
    ''' can create a linked list. '''

    def __init__(self,head=None):
        self.head = head


    def append(self,data):

        new_node = Node(data)
        new_node.set_next_node(self.head)
        self.head = new_node

    def delete(self,data):
        ''' Deletes an instance in the linked list '''

        current_node  = self.head
        previous_node = None
        found         = False
        while not found:

            if current_node.get_data() == data: 
                found = True

            else:
                previous_node = current_node
                current_node  = current_node.get_next()
                print (previous_node,previous_node.get_data())

        if previous_node == None:
            self.head = current_node.get_next()
        else:
            previous_node.set_next_node(current_node.get_next())



    def __str__(self):
        ''' prints out the list. '''
        result =  ' '
        node = self.head
        if node != None:
            while node:
                result += str(node.data) + ','
                node = node.next
        return result



if __name__ == '__main__':
    my_list = Linked_list()

    my_list.append(2)
    my_list.append(4)
    my_list.append(8)
    my_list.append(9)
    my_list.append(2)
    my_list.append(6)
    my_list.append(8)
    print (my_list)
    my_list.delete(2)
    my_list.delete(8)
    print (my_list)

