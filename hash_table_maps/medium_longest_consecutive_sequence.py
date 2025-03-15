class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Can't use "sorted" because of the time complexity.
        
        Create lists of sequences
        """
        """
        from collections import defaultdict
        sequences = defaultdict(int)
        maxval = 0
        for num in nums:
            x = sequences(num-1)
            y = sequences(num+1)
            seq_len = x + y +1
            sequences[num-x] = seq_len
            sequences[num+y] = seq_len
            maxval = max(maxval, seq_len)
        return maxval
        """
        from collections import defaultdict
        sequences = defaultdict(int)
        maxval = 0
        for num in set(nums):
            x = sequences[num-1]
            y = sequences[num+1]
            seq_len = x + y + 1
            sequences[num-x] = seq_len
            sequences[num+y] = seq_len
            maxval = max(maxval, seq_len)
        return maxval
