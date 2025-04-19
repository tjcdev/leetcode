class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value


def postorder(node):
    if(node is not None):
        postorder(node.left)
        postorder(node.right)
        print(node.data)


# https://www.geeksforgeeks.org/iterative-postorder-traversal-using-stack/
def postOrderIterative(root):
    stack = []
    
    while(True):
        while(root != None):
            stack.append(root)
            stack.append(root)
            root = root.left

        # Check for empty stack
        if (len(stack) == 0):
            return
        
        root = stack.pop()

        if (len(stack) > 0 and stack[-1] == root):
            root = root.right
        else:
            print(root.data, end = " ")
            root = None


# My attempt
def postOrderIterative(root):
    stack = []

    while(True):
        while root is not None:
            stack.append(root)
            stack.append(root)
            root = root.left
        
        if len(stack) == 0:
            return

        root = stack.pop()

        if len(stack) > 0  and root == stack[-1]:
            root = root.right
        else:
            print(root.data)
            root = None

        

            

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
postorder(root)

#              4
#          /       \
#         5         6
#       /  \      /   \
#      7   None  None  None
#     / \
# None   None