class Solution(object):
    def maxScore(self, s):
        list_s = list(s)
        scores = []
        for i in range(1,len(list_s)):
            ones, zeros = 0 ,0
            temp1 = list_s[:i]
            for j in temp1:
                if j == '0': 
                    zeros +=1
            temp2 = list_s[i:]
            for j in temp2:
                if j == '1':
                    ones +=1
            scores.append(ones+zeros)
        return max(scores)


        