import math
# Add any extra import statements you may need here
from collections import deque
import numpy as np

# Add any helper functions you may need here
"""
  arr = deque(arr)
  for i in range(x):
    largest_elem = -np.inf
    largest_elem_idx = 0
    temp = []
    for j in range(x):
      if len(arr) > 0:
        elem = arr.popleft()
        if elem > largest_elem:
          largest_elem_idx = j
          largest_elem = elem
        temp.append(elem)
      else:
        break
    del temp[largest_elem_idx]
    for item in temp:
      arr.appendleft(item-1)
  return arr
"""
"""
for i in range(x):
  amount_to_pop = min(x, len(arr))
  popped_elements = arr[:amount_to_pop]
  max_elem = np.argmax(popped_elements)
  del popped_elements[max_elem]
  
  decremented_popped_elements = [elem-1 for elem in popped_elements]
  new_arr = decremented_popped_elements + arr[amount_to_pop:]
  arr = new_arr
  
return arr
"""

"""
  x_1 = 2
  arr_1 = [1, 2, 2, 3, 4, 5]
  
iteration 1:
  amount_to_pop = 2
  popped_elements = [1, 2]
  max_elem = 1
  popped_elements = [1]
  decremented_popped_elements = [0]
  new_arr = [0] + 

  expected: arr_1 = [0, 2, 3, 4, 5]
  
iteration 2:
  expected: arr_1 = [0, 3, 4, 5]
"""

def findPositions(arr, x):
  for i in range(x):
    amount_to_pop = min(x+1, len(arr))
    popped_elements = arr[:amount_to_pop]
    max_elem = np.argmax(popped_elements)

    del popped_elements[max_elem]

    decremented_popped_elements = [elem-1 if elem>0 else elem for elem in popped_elements]
    new_arr = decremented_popped_elements + arr[amount_to_pop:]
    arr = new_arr

  return arr
    
      
  

  









# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
  print('[', n, ']', sep='', end='')

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
  n_1 = 6
  x_1 = 5
  arr_1 = [1, 2, 2, 3, 4, 5]
  expected_1 = [5, 6, 4, 1, 2]
  output_1 = findPositions(arr_1, x_1)
  check(expected_1, output_1)

  n_2 = 13
  x_2 = 4
  arr_2 = [2, 4, 2, 4, 3, 1, 2, 2, 3, 4, 3, 4, 4]
  expected_2 = [2, 5, 10, 13]
  output_2 = findPositions(arr_2, x_2)
  check(expected_2, output_2)
  
  n_3 = 13
  x_3 = 1
  arr_3 = [2, 4, 2]
  expected_3 = [1, 2]
  output_3 = findPositions(arr_3, x_3)
  check(expected_3, output_3)

  # Add your own test cases here
  