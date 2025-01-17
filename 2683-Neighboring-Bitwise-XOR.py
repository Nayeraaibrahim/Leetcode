class Solution(object):
    def doesValidArrayExist(self, derived):
        re = 0
        for i in derived:
            re ^=i
        return re ==0