from typing import List
# Write any import statements here

"""
[9, 4, 4, 8]
[1, 9, 4, 4]

exp=[2, 5, 0, 4]
"""

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
  # Write your code here
  shifted_C = [1] + C[:-1]
  moves = [min((a-b) % N, (b-a) % N) for a, b in zip(C, shifted_C)]
  return sum(moves)