# https://leetcode.com/problems/two-sum/?envType=problem-list-v2&envId=array

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i, num in enumerate(nums):
            if num in indices.keys():
                return [indices[num], i]
            else:
                indices[target-num] = i
        return None