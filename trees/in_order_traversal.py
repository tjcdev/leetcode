class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value

# Recursive
def inorder(node):
    if(node is not None):
        inorder(node.left)
        print(node.data)
        inorder(node.right)


# In Order
# https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion/
def inOrder(root):
    ans = []
    stack = []
    curr = root

    while curr is not None or len(stack) > 0:
        
        # Reach the left most Node of the curr Node
        while curr is not None:
            
            # Place pointer to a tree node on
            # the stack before traversing
            # the node's left subtree
            stack.append(curr)
            curr = curr.left

        # Current must be None at this point
        curr = stack.pop()
        ans.append(curr.data)

        # we have visited the node and its
        # left subtree. Now, it's right
        # subtree's turn
        curr = curr.right

    return ans

# My own practices
def inOrder(root):
    ans = []
    stack = []
    curr = root
    
    while curr is not None and len(stack) > 0:
        while curr is not None:
            stack.append(curr)
            curr = curr.left
        
        curr = stack.pop()
        ans.append(curr)

        curr = curr.right
    
    return ans


# create root
root = Node(4)
''' following is the tree after above statement 
	    4 
	  /   \ 
	None  None
'''

root.left = Node(5)
root.right = Node(6)

''' 5 and 6 become left and right children of 1 
		           4 
		       /       \ 
		      5	        6 
	      /  \      /   \ 
      None None  None  None
'''


root.left.left = Node(7)
'''
7 becomes left child of 5
		           4 
		       /       \ 
		      5	        6 
	      /  \      /   \ 
       7   None  None  None
      / \
  None   None
'''
inorder(root)
