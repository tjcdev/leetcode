from typing import List
# Write any import statements here

"""
You're trying to open a lock. The lock comes with two wheels, each of which has the integers from 
1
1 to 
N
N arranged in a circle in order around it (with integers 
1
1 and 
N
N adjacent to one another). Each wheel is initially pointing at 
1
1.
For example, the following depicts the lock for 
N
=
10
N=10 (as is presented in the second sample case).

It takes 
1
1 second to rotate a wheel by 
1
1 unit to an adjacent integer in either direction, and it takes no time to select an integer once a wheel is pointing at it.
The lock will open if you enter a certain code. The code consists of a sequence of 
M
M integers, the 
i
ith of which is 
C
i
C 
i
​
 . For each integer in the sequence, you may select it with either of the two wheels. Determine the minimum number of seconds required to select all 
M
M of the code's integers in order.
Constraints
3
≤
N
≤
1
,
000
,
000
,
000
3≤N≤1,000,000,000
1
≤
M
≤
3
,
000
1≤M≤3,000
1
≤
C
i
≤
N
1≤C 
i
​
 ≤N
Sample test case #1
N = 3
M = 3
C = [1, 2, 3]
Expected Return Value = 2
Sample test case #2
N = 10
M = 4
C = [9, 4, 4, 8]
Expected Return Value = 6
Sample Explanation
In the first case, there are 
3
3 integers on the locks, and the sequence of integers to be selected is 
[
1
,
2
,
3
]
[1,2,3]. One optimal way to enter the code is: select 
1
1 on the first lock 
→
→ rotate the first lock to 
2
2 (
1
1 second) 
→
→ select 
2
2 
→
→ rotate the second lock from 
1
1 backwards to 
3
3 (
1
1 second) 
→
→ select 
3
3. The total time taken is 
1
+
1
=
2
1+1=2 seconds.
In the second case, the locks each consists of the integers 
1
1 through 
10
10, and the sequence to be selected is 
[
9
,
4
,
4
,
8
]
[9,4,4,8]. One optimal way to enter the code is: rotate the first lock from 
1
1 backwards to 
9
9 (
2
2 seconds) 
→
→ select 
9
9 
→
→ rotate the second lock forwards from 
1
1 to 
4
4 (
3
3 seconds) 
→
→ select 
4
4 twice 
→
→ rotate the first lock from 
9
9 backwards to 
8
8 (
1
1 second) 
→
→ select 
8
8. The total time taken is 
2
+
3
+
1
=
6
2+3+1=6 seconds.
"""

"""
Simple solution would just see "what dial is closest to the next number I need and move that one."

Counter example to this:
Dial1: 3, Dial2: 8, Target:[6, 9]

Dial2 -> 6 (2 seconds) -> 9 (3 seconds) = 5 seconds
Dial1 -> 6 (3 seconds) -> Dial2 9 (1 second) = 4 seconds

It's a depth first search of a tree.

HELPER METHOD
finds the minimum path given:
    - the current node (remaining list of C)
    - current status of dial_1 and dial_2
    - N
 returns:
    - minimum time

"""

"""
N = 10
M = 4
C = [9, 4, 4, 8]

helper([9, 4, 4, 8], 1, 1, 10):
  dial1_cost = 2 + helper([4, 4, 8], 9, 1, N)
    dial1_cost = 

"""

"""FAILED DUE TO RUNTIME"""

def helper(C: List, dial1: int, dial2: int, N: int):
  if len(C) == 0:
    return 0
  
  min_dial_1_turn = min(((dial1 - C[0]) % N), ((C[0] - dial1) % N))
  min_dial_2_turn = min(((dial2 - C[0]) % N), ((C[0] - dial2) % N))
  dial1_cost = min_dial_1_turn + helper(C[1:], C[0], dial2, N)
  dial2_cost = min_dial_2_turn + helper(C[1:], dial1, C[0],  N)
  
  return min(dial1_cost, dial2_cost)

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
  return helper(C, 1, 1, N)


"""" action answer"""
from typing import List
# Write any import statements here

"""
Simple solution would just see "what dial is closest to the next number I need and move that one."

Counter example to this:
Dial1: 3, Dial2: 8, Target:[6, 9]

Dial2 -> 6 (2 seconds) -> 9 (3 seconds) = 5 seconds
Dial1 -> 6 (3 seconds) -> Dial2 9 (1 second) = 4 seconds

It's a depth first search of a tree.

HELPER METHOD
finds the minimum path given:
    - the current node (remaining list of C)
    - current status of dial_1 and dial_2
    - N
 returns:
    - minimum time

"""

"""
N = 10
M = 4
C = [9, 4, 4, 8]

helper([9, 4, 4, 8], 1, 1, 10):
  dial1_cost = 2 + helper([4, 4, 8], 9, 1, N)
    dial1_cost = 

"""
def getMinimalPathLength(N, start, end):
  direct_path_length = abs(end - start)
  return min(direct_path_length, N - direct_path_length)

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
  tree = {
      (C[0], 1): getMinimalPathLength(N, C[0], 1)
  }

  for digit in C[1:]:
    next_tree = {}

    for state in tree.keys():
      left_state = (digit, state[1])
      left_movement = getMinimalPathLength(N, digit, state[0])
      if left_state in next_tree:
          next_tree[left_state] = min(tree[state] + left_movement, next_tree[left_state])
      else:
          next_tree[left_state] = left_movement + tree[state]

      right_state = (state[0], digit)
      right_movement = getMinimalPathLength(N, digit, state[1])
      if right_state in next_tree:
          next_tree[right_state] = min(tree[state] + right_movement, next_tree[right_state])
      else:
          next_tree[right_state] = right_movement + tree[state]

    tree = next_tree

  return min(tree.values())
  

  
