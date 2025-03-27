import math
# Add any extra import statements you may need here
from collections import defaultdict

# Add any helper functions you may need here
"""
Dictionary
  - Key = remainder of k - arr[x]
  - Value = frequency of the remainder
 
Algo:
num_pairs = 0

for v in arr:
  if (k-v) in dictionary and dictionary[(k-v)] >= 1:
    num_pairs += 1
    dictionary[(k-v)] -= 1
  else:
    dictionary[(k-v)] += 1
  
return num_pairs
"""


"""
  k_2 = 6
  arr_2 = [1, 5, 3, 3, 3]
  expected_2 = 4
"""

"""
1: 0
3: 1

"""



def numberOfWays(arr, k):
  num_pairs = 0
  remainders = defaultdict(int)
  
  for v in arr:
    num_pairs += remainders[(k-v)]
    remainders[v] += 1

  return num_pairs
  












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
  k_1 = 6
  arr_1 = [1, 2, 3, 4, 3]
  expected_1 = 2
  output_1 = numberOfWays(arr_1, k_1)
  check(expected_1, output_1)

  k_2 = 6
  arr_2 = [1, 5, 3, 3, 3]
  expected_2 = 4
  output_2 = numberOfWays(arr_2, k_2)
  check(expected_2, output_2)
  
  k_3 = 1
  arr_3 = [1]
  expected_3 = 0
  output_3 = numberOfWays(arr_3, k_3)
  check(expected_3, output_3)

  # Add your own test cases here
  