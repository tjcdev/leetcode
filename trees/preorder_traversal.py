class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value


def preorder(node):
    if(node is not None):
        print(node.data)
        preorder(node.left)
        preorder(node.right)


# Iterative approach
# my attempt

def preOrderIterative(root):
    ans = []
    stack = []
    curr = root
    
    while len(stack) > 0 and curr is not None:
        print(curr.data)

        while curr is not None:
            stack.append(curr)
            curr = curr.left
            print(curr.data)
        
        curr = stack.pop().right

# https://www.geeksforgeeks.org/iterative-preorder-traversal/
def preOrder(root):
    res = []
    if root is None:
        return res

    stack = []
    curr = root

    while stack or curr:
        while curr:
            res.append(curr.data)
            if curr.right:
                stack.append(curr.right)
            curr = curr.left

        if stack:
            curr = stack.pop()

    return res

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
preorder(root)

#              4
#          /       \
#         5         6
#       /  \      /   \
#      7   None  None  None
#     / \
# None   None