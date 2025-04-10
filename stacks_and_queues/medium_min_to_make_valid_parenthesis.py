class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        girl, boys = 0, 0

        for i in range(len(s)):
            if boys > 0 and s[i] == ')':
                # Couple formed, decrease boys count
                boys -= 1
            else:
                if s[i] == '(':
                    boys += 1
                else:
                    girl += 1

        return girl + boys