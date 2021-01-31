class Solution:
    def missingNumber(self, nums):
        nums_sum = sum(nums)
        n = len(nums)
        total_sum = n*(n+1)/2
        
        return int(total_sum - nums_sum)

s = Solution()

print(s.missingNumber([0, 1, 2, 3, 5]))