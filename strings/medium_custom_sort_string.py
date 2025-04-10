"""
Best time complexity for sorting is O(nlogn)

Using dictionary will allow for quick lookup.

- count the frequencies of all letters in the string s
- construct the string again in the order
"""

from collections import defaultdict
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = defaultdict(int)
        for c in s:
            freq[c] += 1
        ans = []
        for o in order:
            ans.append("".join([o for _ in range(freq[o])]))
            freq[o] = 0
        for c, f in freq.items():
            if f > 0:
                ans.append("".join([c for _ in range(f)]))
        return "".join(ans)
        
        