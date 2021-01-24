def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    latest_nonzero_index = 0
    
    for num in nums:
        # If the number is not a zero
        if num != 0:
            # Swap the earlist zero we encountered with the current number
            nums[latest_nonzero_index] = num
            # Replace the current number with 0
            latest_nonzero_index += 1
            # Update the earliest 0 to be the number after the previous
            
    for i in range(latest_nonzero_index, len(nums)):
        nums[i] = 0