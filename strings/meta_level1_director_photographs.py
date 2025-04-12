import numpy


def bounded(i, N):
    return max(0, min(i, N))


def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
  P_cumulative_sum = [0] + list(numpy.cumsum([1 if cell == 'P' else 0 for cell in C]))
  B_cumulative_sum = [0] + list(numpy.cumsum([1 if cell == 'B' else 0 for cell in C]))

  result = 0

  for index, cell in enumerate(C):
      if cell != 'A':
          continue

      left_window = (bounded(index - Y, N), bounded(index - X + 1, N))
      right_window = (bounded(index + X, N), bounded(index + Y + 1, N))

      P_left_count = P_cumulative_sum[left_window[1]] - P_cumulative_sum[left_window[0]]
      B_right_count = B_cumulative_sum[right_window[1]] - B_cumulative_sum[right_window[0]]

      P_right_count = P_cumulative_sum[right_window[1]] - P_cumulative_sum[right_window[0]]
      B_left_count = B_cumulative_sum[left_window[1]] - B_cumulative_sum[left_window[0]]

      result += P_left_count * B_right_count + B_left_count * P_right_count

  return result

"""
My Own answer
"""
import numpy


def bounded(i, N):
    return max(0, min(i, N))


def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
  """
  I'm looking for PAB, or BAP that satisfies the distance constraints of [X, Y]
  
  Iterate through the string, when we a "P", for (Y-X) further into the string looking for an A and, for each A found, then a further Y-X into the string counting the B's.
    Do the same if you encounter a "B".
    Keep score
  
  return score
  """
  distance = Y-X
  opposite = {
    "B": "P",
    "P": "B"
  }
  count = 0
  for n in range(N):
    if C[n] in ["P", "B"]:
      char = C[n]
      for i in range(min(N, n+X), min(N, n+Y+1)): # Looking for A:
        if C[i] == "A":
          for j in range(min(N, i+X), min(N, i+Y+1)): # Looking for pairing
            if C[j] == opposite[char]:
              count += 1
  return count
        
      