'''1. Implement in the language of your choice a function that deletes a node in a binary search tree.
Integrate this function in the code provided to you on Moodle. 
The deletion operation should be
performed based on the key (value) of the node.'''


class BinTreeNode(object):  
  ''' create a Tree Node. '''

  def __init__(self, value):
    self.value	=  value
    self.left 	=  None
    self.right	=  None
      


def tree_insert( tree, item):
  ''' insert a tree '''

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
 
def in_order(tree):
  ''' place the tree in order.'''
  print (tree.value)

  if tree.left!=None:
      in_order(tree.left)

  if tree.right!=None:
      in_order(tree.right)


class Delete_Node(object):
  '''deletes a node from the tree'''

  def __init__ (self,tree):
    self.tree = tree


  def find_node(self,target):

    t = self.tree

    while t != None:
      if t.value == target:
        return True

      elif t.value > target:
        t = t.left

      else:
        t = t.right

    return False

  def count_children(self,tree):
    ''' returns children '''
    count = 0

    self.tree = tree

    if tree.left != None:
      count = count + 1

    if tree.right != None:
      count = count + 1
    return count


  def no_child(self):
    pass

  def one_child(self):
    pass

  def two_children(self):
    pass

  def __str__(self):
    return self.tree


if __name__ == '__main__':

  t=tree_insert(None,6)
  tree_insert(t,10)
  tree_insert(t, 5)
  tree_insert(t, 2)
  tree_insert(t, 3)
  tree_insert(t, 4)
  tree_insert(t,11)
  in_order(t)

  s = Delete_Node(t)
  s.find_node(2)
  s.find_node(5)
  s.find_node(3)
  s.find_node(10)
  s.count_children(3)