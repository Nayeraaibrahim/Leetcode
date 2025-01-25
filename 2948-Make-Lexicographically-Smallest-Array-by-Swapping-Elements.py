class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)
        sp = sorted([(nums[i],i) for i in range(n)])
        res = [0]*n
        s = 0
        for i in range(n):
            if i == n-1 or sp[i+1][0]- sp[i][0] > limit:
                temp = [pair[1] for pair in sp[s:i+1]]
                temp.sort()
                for j in range(len(temp)):
                    res[temp[j]] = sp[s+j][0]
                s = i+1
        return res



        