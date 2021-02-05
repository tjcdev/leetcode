# Time Complexity = O(N)
# Space Complexity = O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None:
            return None
        
        if (root.val == p.val or root.val == q.val):
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if (left == None and right == None):
            return None
        
        if (left != None and right != None):
            return root
        
        if (left!= None and right == None):
            return left
        if (left == None and right != None):
            return right
        