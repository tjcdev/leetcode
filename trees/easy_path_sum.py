# Time Complexity: O(N)
# Space Complexity: O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasSum(self, node, path_sum, target):
        remaining = target - path_sum
        if node is None:
            return False
        if ((node.val == remaining) 
            and (node.left is None) 
            and (node.right is None)):
            return True
        else:
            return max([
                self.hasSum(node.left, path_sum + node.val, target),
                self.hasSum(node.right, path_sum + node.val, target),
            ])
            
            
                
    
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        return self.hasSum(root, 0, targetSum)