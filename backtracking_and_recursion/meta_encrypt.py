import math
# Add any extra import statements you may need here


# Add any helper functions you may need here
"""
helper (substring):
  ans = []
  append the middle character to ans
  append (helper(left substring)) to ans
  append (helper(right substring)) to ans
  return ans
  
"""


def findEncryptedWord(s):
  if len(s) == 0:
    return ""
  
  ans = []
  mid_idx = (len(s) // 2 + len(s) % 2) - 1
  ans.append(s[mid_idx])
  ans.append(findEncryptedWord(s[:mid_idx]))
  ans.append(findEncryptedWord(s[mid_idx+1:]))
  
  return "".join(ans)
  
  











# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printString(string):
  print('[\"', string, '\"]', sep='', end='')

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
    printString(expected)
    print(' Your output: ', end='')
    printString(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  s1 = "abc"
  expected_1 = "bac"
  output_1 = findEncryptedWord(s1)
  check(expected_1, output_1)

  s2 = "abcd"
  expected_2 = "bacd"
  output_2 = findEncryptedWord(s2)
  check(expected_2, output_2)

  # Add your own test cases here
  