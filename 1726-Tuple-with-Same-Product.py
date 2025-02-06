class Solution(object):
    def tupleSameProduct(self, nums):
        c = 0
        a = collections.Counter()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                m = nums[i]*nums[j]
                c += a[m]
                a[m] +=1
        return c*8
        