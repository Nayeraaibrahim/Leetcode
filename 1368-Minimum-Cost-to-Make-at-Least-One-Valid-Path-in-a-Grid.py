class Solution(object):
    def minCost(slef, grid):
        m, n = len(grid), len(grid[0])
        directions = {
            1: (0, 1),   # Right
            2: (0, -1),  # Left
            3: (1, 0),   # Down
            4: (-1, 0)   # Up
        }
        
        pq = [(0, 0, 0)]
        
        visited = [[float('inf')] * n for _ in range(m)]
        visited[0][0] = 0  
        
        while pq:
            cost, i, j = heapq.heappop(pq)
            if i == m - 1 and j == n - 1:
                return cost
            
            for sign, (di, dj) in directions.items():
                ni, nj = i + di, j + dj      
                if 0 <= ni < m and 0 <= nj < n:
                    new_cost = cost + (0 if grid[i][j] == sign else 1)
                    if new_cost < visited[ni][nj]:
                        visited[ni][nj] = new_cost
                        heapq.heappush(pq, (new_cost, ni, nj))
        
        return -1
            
            
        