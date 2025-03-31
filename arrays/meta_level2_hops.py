from typing import List
# Write any import statements here
"""
1 frog can move 1 step at a time
2 frogs can move 2 steps at a time
3 frogs can move 3 steps at a time etc.
"""

"""
N could be 10^12.
So this has to be O(N)

sorted(P) -> O(N log N)

We only care about groupings of frogs. 

Groups of frogs moved at a pace of 1 step per second.

So we are just looking for the intervals between groupings of frogs. The gaps.

Algo. Number 1
[2, 4, 5]
intervals = 1 + 0 = 1
gap to end = (6 - 5) = 1
F-1 = 2

Algo. Number 2
N = 3
F = 1
P = [1]
internals = 0 
gap to end = 3-1 = 2

Algo. Number 3
N = 6
F = 2
[1, 2, 5]
intervals = 0 + 2 = 2
gap to end = (6 - 5) = 1
F-1 = 1
"""
def getSecondsRequired(N: int, F: int, P: List[int]) -> int:
  # Write your code here
  sorted_F = sorted(P)
  
  ans = 0
  for i in range(len(sorted_F)-1):
    ans += (sorted_F[i+1] - sorted_F[i])-1
  
  ans += N - sorted_F[-1]
  
  ans += F-1
  
  return ans
    
    
