# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        # Edge cases
        - all one letter
        - all different letters
        - length = 0
        '''
        
        # Algorithm
        if len(s) == 0:
            return 0
        
        start = 0
        end = 1
        longest_substring = 1
        substring = s[start]
        while (end < len(s)):
            if s[end] not in substring:
                substring = substring + s[end]
                end += 1
            else:
                longest_substring = max([longest_substring, len(substring)])
                start += 1
                substring = substring[1:]
                
        longest_substring = max([longest_substring, len(substring)])
            
        return longest_substring