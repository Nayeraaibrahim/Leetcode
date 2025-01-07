class Solution(object):
    def stringMatching(self, words):
        result = set()
        for i in words:
            for j in words:
                if i != j and i in j:
                    result.add(i)
        return list(result)