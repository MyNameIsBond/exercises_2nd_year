'''
1. Implement in the language of your choice a function that deletes a node in a binary search tree.
Integrate this function in the code provided to you on Moodle. 
The deletion operation should be
performed based on the key (value) of the node.
'''


class BinTreeNode(object):

    def __init__(self, value):
        self.value	=value
        self.left 	=None
        self.right	=None
        


def tree_insert( tree, item):

    if tree==None:
        tree=BinTreeNode(item)

    else:
    	
        if item < tree.value:

            if tree.left==None:
                tree.left=BinTreeNode(item)

            else:
                tree_insert(tree.left,item)
        else:

            if tree.right==None:
                tree.right=BinTreeNode(item)

            else:
                tree_insert(tree.right,item)
    return tree
 
def postorder(tree):

    if tree.left!=None:
        postorder(tree.left)
    if tree.right!=None:
        postorder(tree.right)
    print (tree.value)
 
def in_order(tree):

    if tree.left!=None:
        in_order(tree.left)
    print (tree.value)
    if tree.right!=None:
        in_order(tree.right)

class Delete_Node(object):
  '''deletes a node from the tree'''

  def __init__ (self,tree,value):

    self.tree = tree
    self.value = value


  def find_node(self,target):

    k = self.tree
    while k != None:

      if k.value == target:
        print ("this is the value {}".format(k.value))
        return k.value

      elif k.value > target:
        k = k.left
        print ("this is the left {}".format(k.value))
        return k.value

      else:
        k = k.right
        print ("this is the right {}".format(k.value))
        return k.value


    return False





  def no_child(self):
    if (self.tree.left and self.tree.left) == None:
      return None
  def one_child(self):
    pass

  def two_children(self):
    pass



if __name__ == '__main__':
  t=tree_insert(None,6)
  tree_insert(t,10)
  tree_insert(t, 5)
  tree_insert(t, 2)
  tree_insert(t, 3)
  tree_insert(t, 4)
  tree_insert(t,11)

  s = Delete_Node(t,3)


  in_order(t)