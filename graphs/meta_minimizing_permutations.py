import math
# Add any extra import statements you may need here
from collections import deque

# Add any helper functions you may need here


def minOperations(arr):
  # Write your code here
  arr = "".join([str(x) for x in arr])
  target = "".join([str(x) for x in sorted(arr)])
  q = deque([(0, arr)]) # level, array
  visited = set(arr)
  
  while q:
    # pop from the top of the queue
    # do all reversal permutations 
    # if the reversed permutation is the target
      # return the depth
    # else:
    # add these to the queu
    level, curr = q.popleft()
    
    if curr == target:
      return level
    
    for i in range(len(curr)):
      for j in range(i, len(curr)):
        permutation = curr[:i] + curr[i:j+1][::-1] + curr[j+1:]
        
        if permutation not in visited:
          visited.add(permutation)
          q.append((level+1, permutation))
  return -1
    
  











# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
  print('[', n, ']', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printInteger(expected)
    print(' Your output: ', end='')
    printInteger(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  n_1 = 5
  arr_1 = [1, 2, 5, 4, 3]
  expected_1 = 1
  output_1 = minOperations(arr_1)
  check(expected_1, output_1)

  n_2 = 3
  arr_2 = [3, 1, 2]
  expected_2 = 2
  output_2 = minOperations(arr_2)
  check(expected_2, output_2)
  
  # Add your own test cases here
  