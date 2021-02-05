# This is a recursive algorithm for finding all subsets of an array of numbers

# Time Complexity: HE DIDN'T SAY but I think it is O(N!)
# Space Complexity: I think it is close to O(N!) too

class Solution:
    def solution(self, nums, ans, cur, index):
        if index >= len(nums):
            return
        ans.append(cur[:])
        for i in range(index, len(nums)):
            if nums[i] not in cur:
                cur.append(nums[i])
                self.solution(nums, ans, cur, i)
                cur.pop()
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        cur = []
        self.solution(nums,ans,cur,0)
        return ans