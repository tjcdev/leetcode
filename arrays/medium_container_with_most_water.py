# Time Complexity: O(N)
# Space Complexity: O(1)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        # Edge Cases:
        len(height) = 2
        
        '''
        left = 0
        right = len(height)-1
        max_volume = 0
        while(left < right):
            cur_volume = (right - left) * min([height[right], height[left]])
            if cur_volume > max_volume:
                max_volume = cur_volume
            
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
                
        return max_volume
        