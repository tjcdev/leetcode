# Time Complexity: O(N^2)
# Space Complexity: O(N)

from collections import defaultdict

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        '''
        # Edge Cases:
        N = 0
        
        # Algorithm
        - Find matching pairs between A/B and C/D
        '''
        
        ab_m = defaultdict(int)
        N = len(A)
        
        for i in range(N):
            for j in range(N):
                ab_m[A[i] + B[j]] += 1
                
        num_combinations = 0       
        for i in range(N):
            for j in range(N):
                num_combinations += ab_m[-(C[i] + D[j])]
        
        return num_combinations