class Solution(object):
    def dis (self, cand , k , val):
            return sum(c//val for c in cand)>=k
    def maximumCandies(self, candies, k):
        if sum(candies) < k:
            return 0
        l ,r =1 , max(candies)
        res = 0
        while l<= r:
            mid = (l+r)//2
            if self.dis(candies, k, mid):
                res = mid
                l = mid+1
            else:
                r = mid-1
        return res
        
        
        