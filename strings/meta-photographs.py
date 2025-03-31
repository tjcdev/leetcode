"""
This feels like a double loop. Especially given N <= 200.

Photograph: A between P and B
Artistic: distance between A and P is in range [X, Y]
  and     distance between A and B is in range [X, Y]
"""

"""
Given X, Y. We could generate ALL combinations and match them to the string. But this might double count.

If we double loop through C, character by character we can check. The second loop (at most) can go Y*2 + 1 away.
Loops can only start from P, or B (because if they start with a . then we'll double count)


  num_of_photographs = 0
  C = list(C)
  for i, c in enumerate(C):
    if c in ['P', 'B']:
      found_other = False
      looking_for = "P" if C == "B" else "B"
      for j in range(1, Y*2):
        if C[i+j] == looking_for:
          

    else:
      continue 
"""

"""
Note: Chapter 2 is a harder version of this puzzle. The only difference is a larger constraint on 
N
N.
A photography set consists of 
N
N cells in a row, numbered from 
1
1 to 
N
N in order, and can be represented by a string 
C
C of length 
N
N. Each cell 
i
i is one of the following types (indicated by 
C
i
C 
i
​
 , the 
i
ith character of 
C
C):
If 
C
i
C 
i
​
  = “P”, it is allowed to contain a photographer
If 
C
i
C 
i
​
  = “A”, it is allowed to contain an actor
If 
C
i
C 
i
​
  = “B”, it is allowed to contain a backdrop
If 
C
i
C 
i
​
  = “.”, it must be left empty
A photograph consists of a photographer, an actor, and a backdrop, such that each of them is placed in a valid cell, and such that the actor is between the photographer and the backdrop. Such a photograph is considered artistic if the distance between the photographer and the actor is between 
X
X and 
Y
Y cells (inclusive), and the distance between the actor and the backdrop is also between 
X
X and 
Y
Y cells (inclusive). The distance between cells 
i
i and 
j
j is 
∣
i
−
j
∣
∣i−j∣ (the absolute value of the difference between their indices).
Determine the number of different artistic photographs which could potentially be taken at the set. Two photographs are considered different if they involve a different photographer cell, actor cell, and/or backdrop cell.
Constraints
1
≤
N
≤
200
1≤N≤200
1
≤
X
≤
Y
≤
N
1≤X≤Y≤N
Sample test case #1
N = 5
C = APABA
X = 1
Y = 2
Expected Return Value = 1
Sample test case #2
N = 5
C = APABA
X = 2
Y = 3
Expected Return Value = 0
Sample test case #3
N = 8
C = .PBAAP.B
X = 1
Y = 3
Expected Return Value = 3
Sample Explanation
In the first case, the absolute distances between photographer/actor and actor/backdrop must be between 
1
1 and 
2
2. The only possible photograph that can be taken is with the 
3
3 middle cells, and it happens to be artistic.
In the second case, the only possible photograph is again taken with the 
3
3 middle cells. However, as the distance requirement is between 
2
2 and 
3
3, it is not possible to take an artistic photograph.
In the third case, there are 
4
4 possible photographs, illustrated as follows:
.P.A...B
.P..A..B
..BA.P..
..B.AP..
All are artistic except the first, where the actor and backdrop exceed the maximum distance of 
3
3.
"""