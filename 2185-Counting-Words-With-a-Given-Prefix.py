class Solution(object):
    def prefixCount(self, words, pref):
        l = len(pref)
        count = 0
        for i in words:
            if pref == i[:l]:
                count +=1
        return count
        