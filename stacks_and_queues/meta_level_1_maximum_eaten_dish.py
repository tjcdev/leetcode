from typing import List
# Write any import statements here

from collections import deque, defaultdict

"""
N dishes < list of integers 1-1,000,000
Won't eat a dish if the dish type is in any of previous K dishes 

If you skip a dish, you didn't eat the dish.
"""

"""
O(N) to run through the array once
Use a queue to manage what's in your belly (max length K)
Maintain a dish count using a dictionary
"""

"""
N = 6
D = [1, 2, 3, 1, 2, 1]
K = 2

third dish:
belly [1, 2, 3]

fourth dish:
[2, 3]


"""

def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
  belly = deque()
  belly_count = defaultdict(int)
  ans = 0
  
  for dish in D:
    if len(belly) > K:
      eaten = belly.popleft()
      belly_count[eaten] -= 1
    if belly_count[dish] == 0:
      belly.append(dish)
      belly_count[dish] += 1
      ans += 1
      
  return ans
  
