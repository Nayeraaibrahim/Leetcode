class Solution(object):
    def maxAscendingSum(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        s = nums[0]
        a = []
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                s+=nums[i]
            else:
                a.append(s)
                s=nums[i]
        a.append(s)
        return max(a)

        