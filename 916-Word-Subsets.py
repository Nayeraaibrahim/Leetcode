class Solution(object):
    def wordSubsets(self, words1, words2):
        result = []
        c = Counter()
        for i in words2:
            c |= Counter(i)
        for i in words1:
            if not (c-Counter(i)):
                result.append(i)
        return result