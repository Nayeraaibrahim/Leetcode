class Solution(object):
    def vowelStrings(self, words, queries):
        vowels = {'a', 'e', 'i', 'o', 'u'}
        prefix = [0] * (len(words) + 1)
        for i in range(len(words)):
            word = words[i]
            if word[0] in vowels and word[-1] in vowels:
                prefix[i + 1] = prefix[i] + 1
            else:
                prefix[i + 1] = prefix[i]
        result = []
        for l, r in queries:
            result.append(prefix[r + 1] - prefix[l])
        return result
        