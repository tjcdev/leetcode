# Write any import statements here

def getUniformIntegerCountInInterval(A: int, B: int) -> int:
  # Write your code here
  """
  There are only 9(?) uniform numbers for each X digit number.
  e.g. X = 3, the uniform numbers are 111, 222, 333, 444, 555, 666, 777, 888, 999.
  
  So, for the range, (A_number_of_digits, B_number_of_digits) (not inclusive) there are 9 per number.
  Then we need to find out how many are above A, and below B in their respective digits.
  """
  
  number_digits_A = len(str(A))
  number_digits_B = len(str(B))
  
  uniform_numbers = 0
  
  if number_digits_A == number_digits_B:
    base_uniform = int("".join(["1"]*number_digits_A))
    if A % base_uniform == 0:
      uniform_numbers += 1
    uniform_numbers += (B // base_uniform) - (A // base_uniform)
  else:
    uniform_numbers += 9 * (number_digits_B-number_digits_A-1)
    
    base_uniform_A = int("".join(["1"]*number_digits_A))
    base_uniform_B = int("".join(["1"]*number_digits_B))
    if A % base_uniform_A == 0:
      uniform_numbers += 1
    uniform_numbers += 9-(A // base_uniform_A)
    uniform_numbers += (B // base_uniform_B)
  return uniform_numbers
