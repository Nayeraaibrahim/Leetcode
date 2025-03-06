class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        c = []
        n=len(grid)**2
        t,r = 0,0
        for i in grid:
            for j in i:
                c.append(j)
                r+=j
        for i in range(1, n+1):
            t+=i
        s = set(c)
        ss = sum(s)
        return [r-ss , t-ss]

        
        