class Solution(object):
    def waysToSplitArray(self, nums):
        total = sum(nums)
        left = 0
        count = 0
        for i in range(len(nums)-1):
            left += nums[i]
            right = total - left
            if left >= right:
                count +=1
        return count

        