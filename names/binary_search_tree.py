"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from collections import deque

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
            # compare the value to the root's value to determine which direction
            # we're gonna go in 
            # if the value < root's value 
        if value < self.value:
                # go left 
                # how do we go left?
                # we have to check if there is another node on the left side
            if self.left: 
                    # then self.left is a Node 
                    # now what?
                self.left.insert(value)
            else:
                    # then we can park the value here
                self.left = BSTNode(value)
            # else the value >= root's value 
        else:
                # go right
                # how do we go right? 
                # we have to check if there is another node on the right side 
            if self.right:
                    # then self.right is a Node 
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target > self.value:
            if self.right:
                return self.right.contains(target)
        elif target < self.value:
            if self.left:
                return self.left.contains(target)
        else:
            return False
        
        # elif target == self.left:
        #     return True                   
        # elif target == self.right:
        #     return True
        # elif target < self.left:
        #     self.left.contains(value)
        # elif target < self.right:
        #     self.right.contains(value)
        # else:
        #     return False
        

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value


    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)
        

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        node = self.value

        if self.left:
            self.left.in_order_print(node)
        print(node)
        if self.right:
            self.right.in_order_print(node)
  
        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node=None):
        #breadth-first-traversal
        node = deque()
        node.append(self)
        while len(node) > 0:
            current = node.popleft()
            print(current.value)
            if current.left:
                node.append(current.left)
            if current.right:
                node.append(current.right)
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        node = []
        node.append(self)
        while len(node) > 0:
            current = node.pop()
            print(current.value)
            if current.right:
                node.append(current.right)
            if current.left:
                node.append(current.left)

   

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        node = self.value
        print(node)
        if self.left:
            self.left.pre_order_dft(node)
        
        if self.right:
            self.right.pre_order_dft(node)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        node = self.value
        
        if self.left:
            self.left.post_order_dft(node)
        
        if self.right:
            self.right.post_order_dft(node)
        print(node)
#       1.
#          8.
#       5.
#   3.      7.
# 2.  4.  6.     

# bst =BSTNode(1)
# bst.insert(8)
# bst.insert(5)
# bst.insert(7)
# bst.insert(6)
# bst.insert(3)
# bst.insert(4)
# bst.insert(2)

# print(bst.value.for_each(fn))

# x = [2,3,4,5,2]

# y = set(x)

# print(list(y))