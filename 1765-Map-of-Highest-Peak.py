class Solution(object):
    def highestPeak(self, isWater):
        rows,cols = len(isWater), len(isWater[0]) 
        visit = [[-1] * cols for _ in range(rows)]
        q = deque()
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        for r in range(rows):
            for c in range(cols):
                if isWater[r][c] == 1:
                    visit[r][c] = 0
                    q.append((r,c))

        
        while q:
            r,c = q.popleft()
            for dr, dc in directions:
                row , col = r+dr , c+dc
                if 0 <=row<rows and 0<=col<cols and visit[row][col] == -1:
                    visit[row][col] = visit[r][c] +1
                    q.append((row,col))
        return visit
