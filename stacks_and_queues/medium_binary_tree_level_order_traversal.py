# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Time Complexity: O(N) (results of going over the nodes once in a BFS fashion)
# Space Complexity: O(N)

from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []

        if(root is None):
            return ans
        
        q = deque([root])

        while(q):
            n = len(q)
            temp = []
            for i in range(0,n):
                f = q.popleft()
                temp.append(f.val)

                if(f.left is not None):
                    q.append(f.left)
                if(f.right is not None):
                    q.append(f.right)

            if(len(temp)>0):
                ans.append(temp[:])
                temp.clear()
        return ans