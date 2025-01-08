class Solution(object):
    def countPrefixSuffixPairs(self, words):
        count = 0 
        def isPrefixAndSuffix(str1, str2):
            chars = len(str1)
            return str1 == str2[:chars] and str1 == str2[-chars:] and len(str2)>= len(str1)

        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if isPrefixAndSuffix(words[i], words[j]):
                    count += 1
        return count