class Solution(object):
    def coloredCells(self, n):
        if n>0:
            c = 1
            for i in range(2,n+1):
                c+= 4*(i-1)
        else:return 0 
        return c

        