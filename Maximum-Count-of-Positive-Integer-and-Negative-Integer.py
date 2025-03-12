class Solution(object):
    def maximumCount(self, nums):
        n = len(nums)
        l ,h = 0 , n-1
        while l<=h:
            mid = l + (h - l) // 2
            if nums[mid] > 0:
                h = mid-1
            else:
                l = mid +1
        p = n-l
        l , h= 0 , n-1
        while l<=h:
            mid = l + (h - l) // 2
            if nums[mid] < 0:
                l = mid +1
            else:
                h = mid-1
        n = h+1
        return max(p,n)

        