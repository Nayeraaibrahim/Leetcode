class Solution(object):
    def findMaxFish(self, grid):
        def Sum(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return 0

            s = grid[r][c]
            grid[r][c] = 0

            for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                s += Sum(nr, nc)

            return s                

        m, n = len(grid), len(grid[0])
        result = 0
        for r in range(m):
            for c in range(n):
                result = max(result, Sum(r, c))

        return result 