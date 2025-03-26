import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


"""
- intuition says that we are looking for cycles
- brute force would be that we just go through the array cycles, counting up signatures as we go.
- Find all cycles, and then count the length of these cycles.
"""

"""
ans = []

for i in range(arr):
  
"""

def findSignatureCounts(arr):
  # Write your code here
  def FindSignatureCounts(bookHolders):
    signCounts = [0] * len(bookHolders)
    rootIndices = [-1] * len(bookHolders)
    visitedStudents = set()
    
    for idx, student in enumerate(bookHolders):
        if student in visitedStudents:
            continue

        visitedStudents.add(student)
        # This is the root of the new passing cycle. Count from 1
        signCounts[idx] = 1
        nextIdx = student - 1

        # Loop till we complete the cycle
        while nextIdx != idx:
            # Update the count at root of the cycle
            signCounts[idx] += 1
            # Refer to the root of the cycle
            rootIndices[nextIdx] = idx
            nextIdx = bookHolders[nextIdx] - 1
            visitedStudents.add(bookHolders[nextIdx])

    for idx in range(len(bookHolders)):
        if rootIndices[idx] != -1:
            # Find count from the root of the cycle
            signCounts[idx] = signCounts[rootIndices[idx]]

    return signCounts
  









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
  arr_1 = [2, 1]
  expected_1 = [2, 2]
  output_1 = findSignatureCounts(arr_1)
  check(expected_1, output_1)

  arr_2 = [1, 2]
  expected_2 = [1, 1]
  output_2 = findSignatureCounts(arr_2)
  check(expected_2, output_2)


  # Add your own test cases here
  