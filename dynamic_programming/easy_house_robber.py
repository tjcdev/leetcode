# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        dp = []
        dp.append(nums[0])
        dp.append(max([nums[1], dp[0]]))
        
        for i in range(2, len(nums)):
            dp.append(max([nums[i] + dp[i-2], dp[i-1]]))
        
        return dp[-1]
                        