class Solution(object):
    def canConstruct(self, s, k):
        if len(s) < k:
            return False
        c = Counter(s)
        counter = 0 
        for i in c.values():
            if i%2:
                counter+=1
        if counter > k:
            return False
        return True
                
        