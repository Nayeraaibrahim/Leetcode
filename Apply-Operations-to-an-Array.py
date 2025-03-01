class Solution(object):
    def applyOperations(self, nums):
        res = []
        c=0
        for i in range(len(nums)):
            if i<len(nums)-1 and nums[i] == nums[i+1]:
                nums[i] = nums[i]*2
                nums[i+1] = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                res.append(nums[i])
            else:
                c+=1 
        for i in range(c):
            res.append(0)
        return res

            