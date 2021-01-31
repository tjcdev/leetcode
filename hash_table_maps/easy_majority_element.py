from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        m = defaultdict(int)
        for i in range(0, len(nums)):
            m[nums[i]] += 1
            if m[nums[i]] > n/2:
                return nums[i]