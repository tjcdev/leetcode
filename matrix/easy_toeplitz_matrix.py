from collections import defaultdict
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        """
        What do all the elements in the top-left to bottom-right diagonals have in common.

        Example 1 indices:
        1-> [0, 0], [1, 1], [2, 2] << it's the different between the indices
        5-> [1, 0], [2, 1]
        2 -> [0, 1], [1, 2]
        """
        # Loop through all the possible indices
        m = len(matrix[0])
        n = len(matrix)
        diagonal_vs = defaultdict(set)
        for i in range(m):
            for j in range(n):
                indice_diff = i-j
                val = matrix[j][i]
                diagonal_vs[indice_diff].add(val)
                if len(diagonal_vs[indice_diff]) > 1:
                    return False
        return True