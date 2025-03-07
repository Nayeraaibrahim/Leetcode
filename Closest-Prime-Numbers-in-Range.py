class Solution(object):
    def closestPrimes(self, left, right):
        def primes(n):
            is_prime = [True]*(n+1)
            is_prime[0] = False
            is_prime[1] = False
            for i in range(2,int(n**0.5)+1):
                if is_prime[i]:
                    for x in range(i*i,n+1,i):
                        is_prime[x]=False
            return is_prime

        pr_list = primes(right)
        pr_range = [i for i in range(left,right+1) if pr_list[i]]
        if len(pr_range) <2:
            return [-1,-1]
        res = [pr_range[0],pr_range[1]]

        for i in range(1,len(pr_range)-1):
            if pr_range[i+1]-pr_range[i]< res[1]-res[0]:
                res = [pr_range[i],pr_range[i+1]]
        return res



        