import math
# Add any extra import statements you may need here
import numpy as np

# Add any helper functions you may need here



"""
Notes:
- Milestones is not gauranteed to be sorted

Example:
[1, 2, 3]
[3, 1]

Go through the revenues and create a running total
Perform a binary search for each milestone, we're looking for an element where cumsum[i] >= milestone, cumsum[i-1] < milestone
"""
def binary_search(arr, low, high, milestone):
  # Check base case
  if high >= low:

      mid = (high + low) // 2
      
      # Is arr[mid] >= milestone
        # Is arr[mid-1] < milestone:
          # Return mid
        # binary search left hand side
      if arr[mid] >= milestone:
        if mid-1 < 0:
          return mid+1
        elif arr[mid-1] < milestone:
          return mid+1
        else:
          return binary_search(arr, low, mid - 1, milestone)
      else:
        return binary_search(arr, mid + 1, high, milestone)

  else:
      # Element is not present in the array
      return -1

def getMilestoneDays(revenues, milestones):
  cumsum_revs = list(np.cumsum(revenues))
  ans = []
  for milestone in milestones:
    ans.append(binary_search(cumsum_revs, 0, len(cumsum_revs) - 1, milestone))
  return ans
  
  
  
  
  
  
  
  
  
  
  

# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printIntegerList(array):
  size = len(array)
  print('[', end='')
  for i in range(size):
    if i != 0:
      print(', ', end='')
    print(array[i], end='')
  print(']', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  expected_size = len(expected)
  output_size = len(output)
  result = True
  if expected_size != output_size:
    result = False
  for i in range(min(expected_size, output_size)):
    result &= (output[i] == expected[i])
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printIntegerList(expected)
    print(' Your output: ', end='')
    printIntegerList(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  revenues_1 = [100, 200, 300, 400, 500]
  milestones_1 = [300, 800, 1000, 1400]
  expected_1 = [2, 4, 4, 5]
  output_1 = getMilestoneDays(revenues_1, milestones_1)
  check(expected_1, output_1)

  revenues_2 = [700, 800, 600, 400, 600, 700]
  milestones_2 = [3100, 2200, 800, 2100, 1000] 
  expected_2 = [5, 4, 2, 3, 2]
  output_2 = getMilestoneDays(revenues_2, milestones_2)
  check(expected_2, output_2)

  # Add your own test cases here
  