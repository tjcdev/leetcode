from typing import List
# Write any import statements here

"""
A cafeteria table consists of a row of 
N
N seats, numbered from 
1
1 to 
N
N from left to right. Social distancing guidelines require that every diner be seated such that 
K
K seats to their left and 
K
K seats to their right (or all the remaining seats to that side if there are fewer than 
K
K) remain empty.
There are currently 
M
M diners seated at the table, the 
i
ith of whom is in seat 
S
i
S 
i
​
 . No two diners are sitting in the same seat, and the social distancing guidelines are satisfied.
Determine the maximum number of additional diners who can potentially sit at the table without social distancing guidelines being violated for any new or existing diners, assuming that the existing diners cannot move and that the additional diners will cooperate to maximize how many of them can sit down.
Please take care to write a solution which runs within the time limit.
Constraints
1
≤
N
≤
1
0
15
1≤N≤10 
15
 
1
≤
K
≤
N
1≤K≤N
1
≤
M
≤
500
,
000
1≤M≤500,000
M
≤
N
M≤N
1
≤
S
i
≤
N
1≤S 
i
​
 ≤N
Sample test case #1
N = 10
K = 1
M = 2
S = [2, 6]
Expected Return Value = 3
Sample test case #2
N = 15
K = 2
M = 3
S = [11, 6, 14]
Expected Return Value = 1
Sample Explanation
In the first case, the cafeteria table has 
N
=
10
N=10 seats, with two diners currently at seats 
2
2 and 
6
6 respectively. The table initially looks as follows, with brackets covering the 
K
=
1
K=1 seat to the left and right of each existing diner that may not be taken.
  1 2 3 4 5 6 7 8 9 10
  [   ]   [   ]
Three additional diners may sit at seats 
4
4, 
8
8, and 
10
10 without violating the social distancing guidelines.
In the second case, only 
1
1 additional diner is able to join the table, by sitting in any of the first 
3
3 seats.
"""

"""
We basically just need to look at the intervals.
If we sorted S, it'd be easy O(NlogN)

Because N could be 10^15, I don't want to have an array that stores the whole array

If K = 3, and S = [2, 12] -> answer = [2, 6, 12]
Person who fits: ((12-2) // (K+1)) - 1

if K = 3, and S = [2, ...]
num_extra_people = 0
if K = 3, and S = [3, ...]
num_extra_people = 0
if K = 3, and S = [4, ...]
num_extra_people = 1
"""

"""
N = 15
K = 2
M = 3
S = [11, 6, 14]

sorted_S = [6, 11, 14]
num_extra_people += 6 // 3 = 2 => 2
"""


def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
  sorted_S = sorted(S)
  num_extra_people = 0
  # Before S starts
  num_extra_people += ((sorted_S[0]-1) // (K+1))

  # During S
  for i in range(M-1):
    start = sorted_S[i]
    end = sorted_S[i+1]
    num_extra_people += ((end-start) // (K+1)) - 1

  
  num_extra_people += ((N-sorted_S[-1]) // (K+1))
  
  return num_extra_people
