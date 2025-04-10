from collections import defaultdict
import random
class Solution:
    """
    - Store nums in a dictionary, where the key=nums[i], value = [i]
    - To get the "equal" probably of returning each index, use random sample.
    """
    def __init__(self, nums: List[int]):
        self.lookup = defaultdict(list)
        for i, num in enumerate(nums):
            self.lookup[num].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.lookup[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)