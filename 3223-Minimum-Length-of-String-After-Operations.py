class Solution(object):
    from collections import Counter
    def minimumLength(self, s):
        c = Counter(s)
        result = 0
        for element, count in c.items():
            if count >= 2 and count % 2 == 0:
                result += 2
            elif (count > 2 and count % 2 != 0) or count == 1:
                result += 1    
        return result





        