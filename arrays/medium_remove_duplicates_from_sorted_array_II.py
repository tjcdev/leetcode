class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        - Gut tells me that this is a pointers exercise
        - Traverse the list once
        - One pointer traverses the whole list
        - Another pointer holds the position you just wrote into
        """
        current = 1
        seq_len = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[current] = nums[i]
                seq_len = 1
                current += 1
            else:
                seq_len += 1
                if seq_len <=2:
                    nums[current] = nums[i]
                    current += 1
            
        return current