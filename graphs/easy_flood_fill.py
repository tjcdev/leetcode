class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        orig_color = image[sr][sc]
        rows, cols = len(image), len(image[0])
        # Performn DFS
        def traverse(r, c):
            visited.add((r, c))
            if image[r][c] == orig_color:
                image[r][c] = color
            else:
                return
            for direction in directions:
                new_r, new_c = r + direction[0], c + direction[1]
                if (new_r, new_c) in visited:
                    continue
                if 0 <= new_r < rows and 0 <= new_c < cols:
                    traverse(new_r, new_c)
        traverse(sr, sc)

        return image

