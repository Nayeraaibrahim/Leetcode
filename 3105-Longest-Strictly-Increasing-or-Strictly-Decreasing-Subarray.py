class Solution(object):
    def longestMonotonicSubarray(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        m = a= d=1
        for i in range(1,n):
            if nums[i] > nums[i-1]:
                a +=1
                d = 1
            elif nums[i]<nums[i-1]:
                d +=1
                a = 1
            else:
                a = d =1
            m = max(m,a,d)
        return m

        