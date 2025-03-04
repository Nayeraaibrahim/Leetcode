class Solution(object):
    def checkPowersOfThree(self, n):
        while n>0:
            r = n%3
            if r == 2:
                return False
            n = n/3
        return True

            
            
        