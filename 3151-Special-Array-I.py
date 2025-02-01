class Solution(object):
    def isArraySpecial(self, nums):
        n = len(nums)
        if n == 1:
            return True
        else:
            res = 0
            for i in range(0,n):
                if i<n-1 and (nums[i]+nums[i+1])%2==1:
                    res +=1
            return res == n-1
                    
                
        
                