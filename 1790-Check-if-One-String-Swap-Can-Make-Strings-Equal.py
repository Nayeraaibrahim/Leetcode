class Solution(object):
    def areAlmostEqual(self, s1, s2):
        if s1 == s2:
            return True
        elif len(s1) == len(s2):
            a = []
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    a.append(i)
            if len(a) == 2 and s1[a[0]] == s2[a[1]] and  s1[a[1]] == s2[a[0]]:
                return True
            else:
                return False
        else:
            return False



                
        