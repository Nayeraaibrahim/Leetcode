class Solution(object):
    def gridGame(self, grid):
        top = sum(grid[0])
        buttom = 0
        min2 = float('inf')
        for i in range(len(grid[0])):
            top -= grid[0][i]
            min2 = min(min2 , max(top, buttom))
            buttom += grid[1][i]
        return min2


        