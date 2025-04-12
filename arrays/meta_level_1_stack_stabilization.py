from typing import List
# Write any import statements here

def getMinimumDeflatedDiscCount(N: int, R: List[int]) -> int:
  """
  Loop through the array backwards.
  If at any moment, the radius of a disc is smaller than the # of remaining slots, return -1
  If the disc is >= the preceding disc, make this disc preceding disk-1
  """
  deflations = 0
  for i in range(len(R)-1, -1, -1):
    if R[i] <= i:
      return -1
    if i == len(R)-1:
      continue
    if R[i] >= R[i+1]:
      deflations += 1
      R[i] = R[i+1]-1
  return deflations
    