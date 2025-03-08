class Solution(object):
    def minimumRecolors(self, blocks, k):
        c,ans = 0,k
        for i in range(len(blocks)):
            if i-k >=0 and blocks[i-k]=="B":
                c-=1
            if blocks[i]=="B":
                c+=1
            ans = min(ans, k-c)    
        return ans
        