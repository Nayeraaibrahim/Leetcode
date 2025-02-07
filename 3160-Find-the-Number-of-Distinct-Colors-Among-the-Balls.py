class Solution(object):
    def queryResults(self, limit, queries):
        ss = defaultdict(set)
        s = {}
        res = []
        for b,c in queries:
            if b not in s:
                s[b] = c
                ss[c].add(b)
            else:
                t = s[b]
                ss[t].remove(b)
                if not ss[t]:
                    del ss[t]
                s[b] = c
                ss[c].add(b)
            res.append(len(ss))
        return res
