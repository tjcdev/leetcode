# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
def isBadVersion(version):
    firstBadVersion = 3
    return version >= firstBadVersion

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # TODO: (kind of) Binary Search through the array
        
        # Edge Cases
        '''
        n = 1 (DONE)
        bad = 1
        bad = n
        '''
        # Edge case if n==1
        if n == 1:
            return 1
        
        left = 1
        right = n
        
        while (left != right):
            # Calculate the midpoint
            midpoint = left + (right - left) // 2
            # Check if the midpoint is a bad version
            if (not isBadVersion(midpoint)):
                left = midpoint + 1
                # right remains the same
            else:
                right = midpoint
                # left remains the same
                
        return left

s = Solution()
answer = s.firstBadVersion(10)
print(answer)