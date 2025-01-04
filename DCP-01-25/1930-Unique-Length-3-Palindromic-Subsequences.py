class Solution(object):
    def countPalindromicSubsequence(self, s):
        count = 0
        for char in set(s):
            first_index = s.find(char)
            last_index = s.rfind(char)
            if first_index < last_index:
                count += len(set(s[first_index+1:last_index]))
        return count