class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i in range(0, len(nums)):
            num = nums[i]
            x = target - num
            if x in m:
                return [m[x], i]
            m[num] = i