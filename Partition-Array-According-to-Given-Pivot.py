class Solution(object):
    def pivotArray(self, nums, pivot):
        res = []
        for i in nums:
            if i < pivot:
                res.append(i)
        for i in nums:
            if i== pivot:
                res.append(i)
        for i in nums:
            if i>pivot:
                res.append(i)  
        return res     