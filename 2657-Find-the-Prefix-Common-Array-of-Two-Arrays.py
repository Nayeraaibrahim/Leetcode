class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        n = len(A)
        result = []
        s = [0] *(n+1)
        c = 0
        for i in range(n):
            if s[A[i]] == 0:
                s[A[i]] = 1
            elif s[A[i]] == 1:
                c +=1
            if s[B[i]] == 0:
                s[B[i]] = 1
            elif s[B[i]] == 1:
                c +=1
            result.append(c)
        return result
            


        