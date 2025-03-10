class Solution(object):
    def countOfSubstrings(self, word, k):
        l, r , c,ans= 0, 0,0,0  
        c = 0  
        vowls ={'u':0, 'o':0, 'i':0, 'a':0, 'e':0}
        for i in word:
            if i in vowls:
                vowls[i]+=1
                if vowls[i] ==1:
                    c+=1
            else:
                k-=1
            while k<0 or c ==5 and vowls.get(word[l],0) >1:
                ch_l = word[l]
                l+=1
                if ch_l in vowls:
                    vowls[ch_l] -=1
                    if vowls[ch_l] == 0:
                        c-=1
                else:
                    k+=1
                    r=l
            if c == 5 and k==0:
                ans+=l-r+1
        return ans

        
        